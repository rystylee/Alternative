s.options.numBuffers = 1024 * 108;
s.options.memSize = 8192 * 16;
s.options.maxNodes = 1024 * 32;
s.options.numOutputBusChannels = 2;
s.options.numInputBusChannels = 2;


s.boot;
s.dumpOSC;

(

SynthDef(\kick, {
	var e0, e1, out;
	e0 = EnvGen.ar(Env.perc(0.001, 0.3), doneAction: 2);
	e1 = EnvGen.ar(Env.new([4000, 200, 40], [0.001, 0.2], [-4, -10]));
	out = LPF.ar(WhiteNoise.ar(1), e1 * 1.5, e0);
	out = out + SinOsc.ar(e1, 0.5, e0);
	Out.ar(0, out.dup);
}).add;

SynthDef(\ckick, {|dur = 0.15, atk = 0.015, amp = 1.5, pan = 0|
	var source;
	source = Pan2.ar(SinOsc.ar(EnvGen.ar(Env(\freq_l.kr([2960, 70, 90]), \freq_d.kr([0.07, 0.15]), \freq_c.kr([-13, -1]))),
		mul:EnvGen.ar(Env.perc( atk, max(dur - atk, atk), curve: \amp_c.kr([-1, 5])), doneAction: 2)), pan, amp);
	Out.ar(0, source);
}).add;


SynthDef(\hihat, {|amp = 0.5, att = 0.01, rel = 0.2, ffreq = 6000, pan = 0|
	var env, snd;
	env = Env.perc(att, rel, amp).kr(doneAction: 2);
	snd = WhiteNoise.ar;
	snd = HPF.ar(in: snd, freq: ffreq, mul: env);
	Out.ar(0, Pan2.ar(snd, pan));
}).add;

SynthDef(\clap, {|amp=1.0|
	var e1, e2, n1, n2, out;
	e1 = EnvGen.ar(Env.new([0, 1, 0, 1, 0, 1, 0, 1, 0], [0.001, 0.013, 0, 0.01, 0, 0.01, 0, 0.03], [0, -3, 0, -3, 0, -3, 0, -4]));
	e2 = EnvGen.ar(Env.perc(0.01, 0.4), doneAction:2);
	n1 = BPF.ar(HPF.ar(WhiteNoise.ar(e1), 600), 2000, 3);
	n2 = BPF.ar(HPF.ar(WhiteNoise.ar(e2), 1000), 1200, 0.7, 0.7);
	out = n1 + n2;
	out = out * amp;
	Out.ar(0, out.dup);
}).add;

SynthDef(\snare, {|amp = 0.5, decay = 0.2, pan = 0.0|
	var env1, env2, out;
	env1 = EnvGen.ar(Env.new([0.5, 1, 0], [0.005, 0.2]), doneAction:2);
	env2 = EnvGen.ar(Env.new([5000, 300, 50], [0.005, 0.05], [-4, -5]));
	out = LFPulse.ar(env2, 0, 0.5);
	out = LPF.ar(out, env2 * 1.5, env1);
	out = out + BPF.ar(WhiteNoise.ar(1), 5000, 0.6) * env1 * amp;
	Out.ar(0, out.dup);
}).add;

SynthDef(\hat, {|amp=0.38, dur=0.3|
	var e1, out;
	e1 = EnvGen.ar(Env.perc(0.0001, dur, 1, -8), doneAction:2);
	out = RHPF.ar(ClipNoise.ar(1), 7000, 0.7) * e1 * amp;
	Out.ar(0, out.dup);
}).add;

SynthDef(\fmchord, {|freq=440, amp=0.2, dur=2|
	var index_env, amp_env, out;
	index_env = EnvGen.ar(Env.perc(0.0001, 0.2, 1, -4));
	amp_env = EnvGen.ar(Env.perc(0.0001, 1, dur, -4), doneAction:2);
	out = PMOsc.ar(freq, freq * 1.02, (index_env * 2)) * amp_env;
	out = FreeVerb.ar(out.dup, 0.5, 0.8, 0.9);
	Out.ar(0, out * amp);
}).add;

SynthDef(\pad, {|freq=440, amp=0.5, dur=2|
	var env1, out;
	env1 = EnvGen.ar(Env.linen(4, 0.3, 4, 1, -4), doneAction:2);
	out = Pulse.ar([freq, freq * 1.01, freq * 0.99], SinOsc.kr(1, 0, 0.3, 1.5), env1);
	out = RLPF.ar(out, freq * 1.1, 0.9);
	out = FreeVerb.ar(out.dup, 0.8, 0.8, 0.9);
	Out.ar(0, out * 0.3);
}).add;

SynthDef(\bass, {|freq=440, ffreq=1000, amp=1.0, dur=2, slew=0.08, gate=1|
	var e1, e2, o;
	e1 = EnvGen.ar(Env.adsr(0.001, 0.1, 0.8, 0.1, 1, -4), gate);
	e2 = EnvGen.ar(Env.adsr(0.001, 0.6, 0.2, 0.4, ffreq, -4), gate);
	o = RLPF.ar(Saw.ar(Lag.kr(freq, slew)), freq + e2, 0.1) * e1;
	Out.ar(0, o.softclip.dup);
}).add;

SynthDef(\piano, {|freq = 440, dur=1.2|
	var out, env, env2;
	env = EnvGen.kr(Env.perc(0.001, dur, 1.0, -4), doneAction: 2);
	out = Mix.ar(Array.fill(3, {|i|
		var detune, delayTime, hammer;
		detune = #[-0.05, 0, 0.04].at(i);
		delayTime = 1 / (freq + detune);
		hammer = LFNoise2.ar(5000, env);
		CombL.ar(hammer, delayTime, delayTime, 2.0);
	})) * 0.1;
	DetectSilence.ar(out, doneAction:2);
	Out.ar(0, out.dup);
}).add

)
