s.boot;
s.dumpOSC;

(

SynthDef("acid_oto309", {
	arg out=0, gate=1, freq=440, amp=0.1, pan=0;
	var env1, env2, son, pitch;
	pitch = freq.cpsmidi;
	pitch = Lag.kr(pitch, 0.12 * (1-Trig.kr(gate, 0.001)) * gate);
	env1 = EnvGen.ar(Env.new([0, 1.0, 0, 0], [0.001, 2.0, 0.04], [0, -4, -4], 2), gate, amp);
	env2 = EnvGen.ar(Env.adsr(0.001, 0.8, 0, 0.8, 70, -4), gate);
	son = LFPulse.ar(pitch.midicps, 0.0, 0.51, 2, -1);

	son = RLPF.ar(son, (pitch + env2).midicps, 0.3);
	son = son * env1;

	Out.ar(out, Pan2.ar(son, pan));
}).add;

SynthDef(\apad_mh, {arg freq=880, amp=0.5, attack=0.4, decay=0.5, sustain=0.8, release=1.0, gate=1.0, out=0;
	var env,sig,mod1,mod2,mod3;
	env=EnvGen.kr(Env.adsr(attack,decay,sustain,release),gate,levelScale:amp,doneAction:2);
	mod1=SinOsc.kr(6).range(freq*0.99,freq*1.01);
	mod2=LFNoise2.kr(1).range(0.2,1);
	mod3=SinOsc.kr(rrand(4.0,6.0)).range(0.5,1);
	sig=SinOsc.ar([freq,mod1],0,env).distort;
	sig=sig*mod2*mod3;
	Out.ar(out,sig);
}).add;

SynthDef(\babblingbrook_jmc, { |out=0, amp=0.1|
	var son;

	son = ({RHPF.ar(OnePole.ar(BrownNoise.ar, 0.99), LPF.ar(BrownNoise.ar, 14)
		* 400 + 500, 0.03, 0.003)}!2)
		+ ({RHPF.ar(OnePole.ar(BrownNoise.ar, 0.99), LPF.ar(BrownNoise.ar, 20)
		* 800 + 1000, 0.03, 0.005)}!2)  * 4;
	Out.ar(out, son * (amp * 20))
}).add;

SynthDef(\cheappiano, { arg out=0, freq=440, amp=0.1, dur=1, pan=0;�
	var sig, in, n = 6, max = 0.04, min = 0.01, delay, pitch, detune, hammer;
	freq = freq.cpsmidi;
	hammer = Decay2.ar(Impulse.ar(0.001), 0.008, 0.04, LFNoise2.ar([2000,4000].asSpec.map(amp), 0.25));
	sig = Mix.ar(Array.fill(3, { arg i;
			detune = #[-0.04, 0, 0.03].at(i);
			delay = (1/(freq + detune).midicps);
			CombL.ar(hammer, delay, delay, 50 * amp)
		}) );

	sig = HPF.ar(sig,50) * EnvGen.ar(Env.perc(0.0001,dur, amp * 4, -1), doneAction:2);
	Out.ar(out, Pan2.ar(sig, pan));
}).add;

SynthDef("clap_oto309", {
	arg out=0, amp = 0.1, pan=0;
	var env1, env2, son, noise1, noise2;

	env1 = EnvGen.ar(Env.new([0, 1, 0, 1, 0, 1, 0, 1, 0], [0.001, 0.013, 0, 0.01, 0, 0.01, 0, 0.03], [0, -3, 0, -3, 0, -3, 0, -4]));
	env2 = EnvGen.ar(Env.new([0, 1, 0], [0.02, 0.3], [0, -4]), doneAction:2);

	noise1 = WhiteNoise.ar(env1);
	noise1 = HPF.ar(noise1, 600);
	noise1 = BPF.ar(noise1, 2000, 3);

	noise2 = WhiteNoise.ar(env2);
	noise2 = HPF.ar(noise2, 1000);
	noise2 = BPF.ar(noise2, 1200, 0.7, 0.7);

	son = noise1 + noise2;
	son = son * 2;
	son = son.softclip * amp;

	Out.ar(out, Pan2.ar(son, pan));
}).add;

SynthDef("cs80lead_mh", {
	arg freq=880, amp=0.5, att=0.75, decay=0.5, sus=0.8, rel=1.0, fatt=0.75, fdecay=0.5, fsus=0.8, frel=1.0,
		cutoff=200, pan=0, dtune=0.002, vibrate=4, vibdepth=0.015, gate=1.0, ratio=1,out=0,cbus=1;
	var env,fenv,vib,ffreq,sig;
	cutoff=In.kr(cbus);
	env=EnvGen.kr(Env.adsr(att,decay,sus,rel),gate,levelScale:1,doneAction:2);
	fenv=EnvGen.kr(Env.adsr(fatt,fdecay,fsus,frel,curve:2),gate,levelScale:1,doneAction:2);
	vib=SinOsc.kr(vibrate).range(-1*vibdepth,vibdepth)+1;
	freq=Line.kr(freq,freq*ratio,5);
	freq=freq*vib;
	sig=Mix.ar(Saw.ar([freq,freq*(1+dtune)],mul:env*amp));
	// keep this below nyquist!!
	ffreq=max(fenv*freq*12,cutoff)+100;
	sig=LPF.ar(sig,ffreq);
	Out.ar(out, Pan2.ar(sig,pan) );
}).add;

SynthDef(\cymbal808_ryan, {
	arg out=0, baseFreq = 300, time = 250, amp=0.1;
	//var freqs = [baseFreq, baseFreq*1.3420, baseFreq*1.2312, baseFreq*1.6532, baseFreq*1.9523, baseFreq*2.1523];
	//var freqs = [78.6, 140.44, 123.87, 219.4, 787.5, 531.3];
	//var freqs = [205.35, 254.29, 294.03, 304.41, 369.64, 522.71];
	var freqs = [205.35, 304.41, 369.64, 522.71, 540.54, 812.21];
	var signal, pulseEnv;

	pulseEnv = EnvGen.ar(Env.new([1.0, 0.6], [time], [-0.5]), timeScale:(1/1000));
	signal = Mix.new(LFPulse.ar(freqs * 4.09));
	signal = (BinaryOpUGen('==', signal, 6.0) * 0.6) + (BinaryOpUGen('==', signal, 2.0) * 0.2) + (BinaryOpUGen('==', signal, 1.0) * 0.9); // XOR
�� 	signal = (signal * pulseEnv) + (Mix.new(LFPulse.ar(freqs, width:0.55)) * 0.9);
�	signal = RLPF.ar(signal, 7000, 0.6);
� 	signal = RHPF.ar(signal, 6800, 1.5);
�	signal = RHPF.ar(signal, 6800, 1.5);
�	signal = RHPF.ar(signal, 1200, 1.5);
	signal = signal + FreeVerb.ar(signal);
	signal = signal * EnvGen.ar(Env.new([0, 1, 0.4, 0, 0], [2, time, 50, 500], [0, -0.5, 0, -50]), timeScale:(1/1000), doneAction:2);
	signal = [signal, DelayN.ar(signal, 0.005, 0.005)];
	OffsetOut.ar(out, signal*4*amp);
}).add;

/*
Based on the example at
http://www.mcld.co.uk/cymbalsynthesis/
published 2008 by Dan Stowell

Synth(\cymbalic_mcld)
*/
SynthDef(\cymbalic_mcld, { |out=0, pan=0, amp=0.1|
	var lodriver, locutoffenv, hidriver, hicutoffenv, freqs, res, thwack;

	locutoffenv = EnvGen.ar(Env.perc(0.5, 5)) * 20000 + 10;
	lodriver = LPF.ar(WhiteNoise.ar(0.1), locutoffenv);

	hicutoffenv = 10001 - (EnvGen.ar(Env.perc(1, 3)) * 10000);
	hidriver = HPF.ar(WhiteNoise.ar(0.1), hicutoffenv);
	hidriver = hidriver * EnvGen.ar(Env.perc(1, 2, 0.25));

	thwack = EnvGen.ar(Env.perc(0.001,0.001,1));

	// This bit will regenerate new freqs every time you evaluate the SynthDef!
	freqs  = {exprand(300, 20000)}.dup(100);

	res    = Ringz.ar(lodriver + hidriver + thwack, freqs).mean;

	Out.ar(out, Pan2.ar(((res * 1) + (lodriver * 2) + thwack) * amp, pan));
}).add;

// a kick made using what radio folks would call a "chirp"
SynthDef(\kick_chrp, { |out=0, amp=0.1, pan=0|
	var ampenv, pitchenv;
	ampenv   = EnvGen.ar(Env.perc(0, 0.2, curve: 0), doneAction: 2);
	pitchenv = EnvGen.ar(Env.perc(0, 0.1, curve: -20).exprange(0, 1000), doneAction: 0);
	Out.ar(out, Pan2.ar(SinOsc.ar(pitchenv) * amp, pan))
}).add;

SynthDef("kick_oto309", {
	arg out=0, amp=0.1, pan=0;
	var env0, env1, env1m, son;

	env0 =  EnvGen.ar(Env.new([0.5, 1, 0.5, 0], [0.005, 0.06, 0.26], [-4, -2, -4]), doneAction:2);
	env1 = EnvGen.ar(Env.new([110, 59, 29], [0.005, 0.29], [-4, -5]));
	env1m = env1.midicps;

	son = LFPulse.ar(env1m, 0, 0.5, 1, -0.5);
	son = son + WhiteNoise.ar(1);
	son = LPF.ar(son, env1m*1.5, env0);
	son = son + SinOsc.ar(env1m, 0.5, env0);

	son = son * 1.2;
	son = son.clip2(1);

	Out.ar(out, Pan2.ar(son * amp));
}).add;

SynthDef(\oneclap_thor, {arg out=0, t_trig=1, amp=0.1, filterfreq=100, rq=0.1, pan=0;
	var env, signal, attack,� noise, hpf1, hpf2;
	noise = WhiteNoise.ar(1)+SinOsc.ar([filterfreq/2,filterfreq/2+4 ], pi*0.5, XLine.kr(1,0.01,4));
	//noise = PinkNoise.ar(1)+SinOsc.ar([(filterfreq)*XLine.kr(1,0.01,3), (filterfreq+4)*XLine.kr(1,0.01,3) ], pi*0.5, XLine.kr(1,0.01,4));
	//signal = signal * SinOsc.ar(1,0.75);
	hpf1 = RLPF.ar(noise, filterfreq, rq);
	hpf2 = RHPF.ar(noise, filterfreq/2, rq/4);
	env = EnvGen.kr(Env.perc(0.003, 0.00035));
	signal = (hpf1+hpf2) * env;
	signal = CombC.ar(signal, 0.5, 0.03, 0.031)+CombC.ar(signal, 0.5, 0.03016, 0.06);
	//signal = Decay2.ar(signal, 0.5);
	signal = FreeVerb.ar(signal, 0.23, 0.15, 0.2);
	Out.ar(out, Pan2.ar(signal * amp, pan));
	DetectSilence.ar(signal, doneAction:2);
}).add;

SynthDef(\ping_mh,{arg freq=440,amp=0.2,dur=1,attack=0.001,pan=0,out=0;
    var sig,freq2;
    freq=freq*rrand(1,1.01);
    freq2=freq*rrand(1,1.01);
    e=EnvGen.ar(Env.perc(attack,dur,curve:-4),doneAction:2);
    sig=SinOsc.ar([freq,freq2],0,amp*e);
    sig=Pan2.ar(sig,pan);
    Out.ar(out,sig)
}).add;

SynthDef("snare_oto309", {
	arg out=0, amp=0.1, pan=0;
	var env0, env1, env2, env1m, oscs, noise, son;

	env0 = EnvGen.ar(Env.new([0.5, 1, 0.5, 0], [0.005, 0.03, 0.10], [-4, -2, -4]));
	env1 = EnvGen.ar(Env.new([110, 60, 49], [0.005, 0.1], [-4, -5]));
	env1m = env1.midicps;
	env2 = EnvGen.ar(Env.new([1, 0.4, 0], [0.05, 0.13], [-2, -2]), doneAction:2);

	oscs = LFPulse.ar(env1m, 0, 0.5, 1, -0.5) + LFPulse.ar(env1m * 1.6, 0, 0.5, 0.5, -0.25);
	oscs = LPF.ar(oscs, env1m*1.2, env0);
	oscs = oscs + SinOsc.ar(env1m, 0.8, env0);

	noise = WhiteNoise.ar(0.2);
	noise = HPF.ar(noise, 200, 2);
	noise = BPF.ar(noise, 6900, 0.6, 3) + noise;
	noise = noise * env2;

	son = oscs + noise;
	son = son.clip2(1) * amp;

	Out.ar(out, Pan2.ar(son, pan));
}).add;

SynthDef(\snare_stein, { |out=0, amp=0.1, pan=0|
var snare, filtWhite;

filtWhite = LPF.ar(WhiteNoise.ar(1), 7040, 1);

snare = ((SinOsc.ar(330,0,0.25) * EnvGen.ar(Env.perc(0.0005,0.055)))
		� � � � � � � � � � � �+(SinOsc.ar(185,0,0.25) * EnvGen.ar(Env.perc(0.0005,0.075)))
		� � � � � � � � � � � �+(filtWhite * EnvGen.ar(Env.perc(0.0005,0.2), doneAction: 2) * 0.2)
		� � � � � � � � � � � �+(HPF.ar(filtWhite, 523, 1) * EnvGen.ar(Env.perc(0.0005,0.183)) * 0.2)
		� � � � � � � � � � � �);
	Out.ar(out, Pan2.ar(snare * amp * 10, pan));

}).add;

SynthDef(\sos_bell, { |freq=440, out=0, amp=0.1, pan=0|
	var son, strike, hum;
	// Stretched harmonic series
	son = SinOsc.ar(#[2, 3, 4.1, 5.43, 6.8, 8.21] * freq, 0,
		 #[1, 0.9, 0.8, 0.7, 0.6, 0.5] * 0.1);

	son = son * EnvGen.ar(Env.new([0,1,0.3, 0.2, 0], [0, 0.3, 0.3, 0.3]));
	// A bit of FM adds 'warble'
	son = son * LFTri.ar({Rand(1.0, 1.8)}.dup(6), 1, 0.3, 0.7);
	// Mix down the partials in the main sound
	son = son.mean;
	strike = SinOsc.ar(LFNoise1.ar(freq * 36, 100, freq*8), 1, 0.1) *
			EnvGen.ar(Env.new([0,1,0.2, 0.1, 0], [0, 0.01, 0, 0.04]));
	hum = SinOsc.ar([freq*1.01, freq*0.47], 0, EnvGen.ar(Env.new([0,0.05,0.05,0], [0.5,0.5,1]), doneAction:2)).mean;
	Out.ar(out, Pan2.ar((son + strike + hum) * 4 * amp, pan));
}).add;




SynthDef("PMCrotale", {
	arg freq = 261, tone = 3, art = 1, amp = 0.8, pan = 0;
	var env, out, mod;
	env = Env.perc(0, art);
	mod = 5 + (1/IRand(2, 6));
	out = PMOsc.ar(freq, mod*freq,
	pmindex: EnvGen.kr(env, timeScale: art, levelScale: tone),
	mul: EnvGen.kr(env, timeScale: art, levelScale: 0.3));
	out = Pan2.ar(out, pan);
	out = out * EnvGen.kr(env, timeScale: 1.3*art,
	levelScale: Rand(0.1, 0.5), doneAction:2);
	Out.ar(0, out*amp); //Out.ar(bus, out);
}).add;





SynthDef("kick3", {arg punch = 1, amp = 1;
    var freq = EnvGen.kr(Env([400, 66], [0.08], -3)),
	sig = Normalizer.ar(SinOsc.ar(freq, 0.5pi, punch).distort, 1) * amp
            * EnvGen.kr(Env([0, 1, 0.8, 0], [0.01, 0.1, 0.2]), doneAction: 2);
    Out.ar(0, sig ! 2);
}).add;

SynthDef("ringkick", {arg freq = 40, decay = 0.25, amp = 1;
	var snd;
	snd = Ringz.ar(
		in: LPF.ar(
			in: Impulse.ar(0),
			freq: 1000),
		freq: freq,
		decaytime: decay,
		mul: 7 * amp).tanh.sin*2;
	Out.ar(0, snd!2);
}).add;

SynthDef("beating", {arg freq = 440, amp = 0.1, art = 1;
	var env, snd1, snd2;
	env = EnvGen.ar(Env.perc(0.01, art), doneAction: 2);
	snd1 = SinOsc.ar(freq);
	snd2 = SinOsc.ar(Line.kr(freq+15, freq, art));
	Out.ar(0, Pan2.ar(Mix([snd1, snd2]), 0, amp*env))
}).add;

SynthDef("bass", { |freq = 440, gate = 1, amp = 0.5, slideTime = 0.17, ffreq = 1100, width = 0.15, detune = 1.005, preamp = 4|
    var sig, env;
	env = Env.adsr(0.01, 0.3, 0.4, 0.1);
    freq = Lag.kr(freq, slideTime);
    sig = Mix(VarSaw.ar([freq, freq * detune], 0, width, preamp)).distort;
	sig = sig * amp * EnvGen.kr(env, gate, doneAction: 2);
    sig = LPF.ar(sig, ffreq);
    Out.ar(0, sig ! 2)
}).add;

SynthDef("kik", { |basefreq = 50, ratio = 7, sweeptime = 0.05, preamp = 1, amp = 1, decay1 = 0.3, decay1L = 0.8, decay2 = 0.15, out|
    var fcurve = EnvGen.kr(Env([basefreq * ratio, basefreq], [sweeptime], \exp)),
        env = EnvGen.kr(Env([1, decay1L, 0], [decay1, decay2], -4), doneAction: 2),
        sig = SinOsc.ar(fcurve, 0.5pi, preamp).distort * env * amp;
    Out.ar(out, sig ! 2)
}).add;

SynthDef("kraftySnr", { |amp = 1, freq = 2000, rq = 3, decay = 0.3, pan, out|
	var sig = PinkNoise.ar(amp),
	env = EnvGen.kr(Env.perc(0.01, decay), doneAction: 2);
	sig = BPF.ar(sig, freq, rq, env);
	Out.ar(out, Pan2.ar(sig, pan))
}).add;

SynthDef("sillyVoice", { arg
	freq = 220,
	amp = 0.5,
	vibratoSpeed = 6,
	vibratoDepth = 4,
	vowel = 0,
	att = 0.01,
	rel = 0.1,
	lag = 1,
	gate = 1;

	var in, vibrato, env, va, ve, vi, vo, vu, snd;

	vibrato = SinOsc.kr(vibratoSpeed, mul: vibratoDepth);
	in = Saw.ar(Lag.kr(freq, lag) + vibrato);
	env = EnvGen.kr(Env.asr(att, 1, rel), gate, doneAction: 2);

	va = BBandPass.ar(
		in: in,
		freq: [ 600, 1040, 2250, 2450, 2750 ],
		bw: [ 0.1, 0.067307692307692, 0.048888888888889, 0.048979591836735, 0.047272727272727 ],
		mul: [ 1, 0.44668359215096, 0.35481338923358, 0.35481338923358, 0.1 ]);

	ve = BBandPass.ar(
		in: in,
		freq: [ 400, 1620, 2400, 2800, 3100 ] ,
		bw: [ 0.1, 0.049382716049383, 0.041666666666667, 0.042857142857143, 0.038709677419355 ],
		mul: [ 1, 0.25118864315096, 0.35481338923358, 0.25118864315096, 0.12589254117942 ]);

	vi = BBandPass.ar(
		in: in,
		freq: [ 250, 1750, 2600, 3050, 3340 ] ,
		bw: [ 0.24, 0.051428571428571, 0.038461538461538, 0.039344262295082, 0.035928143712575 ],
		mul: [ 1, 0.031622776601684, 0.15848931924611, 0.079432823472428, 0.03981071705535 ] );

	vo = BBandPass.ar(
		in: in,
		freq:[ 400, 750, 2400, 2600, 2900 ] ,
		bw: [ 0.1, 0.10666666666667, 0.041666666666667, 0.046153846153846, 0.041379310344828 ],
		mul: [ 1, 0.28183829312645, 0.089125093813375, 0.1, 0.01 ]);

	vu = BBandPass.ar(
		in: in,
		freq: [ 350, 600, 2400, 2675, 2950 ],
		bw: [ 0.11428571428571, 0.13333333333333, 0.041666666666667, 0.044859813084112, 0.040677966101695 ],
		mul: [ 1, 0.1, 0.025118864315096, 0.03981071705535, 0.015848931924611 ]);

	snd = SelectX.ar(Lag.kr(vowel, lag), [va, ve, vi, vo, vu]);
	snd = Mix.new(snd);
	Out.ar(0, snd!2 * env * amp);
}).add;

SynthDef("plucking", {arg amp = 0.1, freq = 440, decay = 5, coef = 0.1;
	var env, snd;
	env = EnvGen.kr(Env.linen(0, decay, 0), doneAction: 2);
	snd = Pluck.ar(
        in: WhiteNoise.ar(amp),
        trig: Impulse.kr(0),

        maxdelaytime: 0.1,
        delaytime: freq.reciprocal,
        decaytime: decay,
        coef: coef);
    Out.ar(0, [snd, snd]);
}).add;

SynthDef("defaultB", { arg out=0, freq=440, amp=0.1, pan=0, gate=1;
    var z;
    z = LPF.ar(
            Mix.new(VarSaw.ar(freq + [0, Rand(-0.4,0.0), Rand(0.0,0.4)], 0, 0.3)),
            XLine.kr(Rand(4000,5000), Rand(2500,3200), 1)
        ) * Linen.kr(gate, 0.01, 0.7, 0.3, 2);
    OffsetOut.ar(out, Pan2.ar(z, pan, amp));
}, [\ir]).add;

SynthDef("trig_demo", { |freq = 440, gate = 1, t_trig = 1|
    var env, sig;
	env = Decay2.kr(t_trig, 0.01, 0.1);
    sig = SinOsc.ar(freq, 0, env);
	sig = sig * Linen.kr(gate, 0.01, 0.1, 0.1, doneAction: 2);
    Out.ar(0, sig ! 2)
}).add;

)