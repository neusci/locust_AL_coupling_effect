package main

import (
	"fmt"
	"math"
	"math/rand"
)

const (
	neuron_num_coefs       = 0.1  // 1: 830-300-330-120;;; 0.1; 0.5; 1; 5; 10; ...
	ms_per_second    int64 = 1000 // 1000 ms = 1 S
	time_len         int64 = 10 * ms_per_second
	PN_number        int64 = 830 * neuron_num_coefs
	LN_number        int64 = 300 * neuron_num_coefs
	stim_PN_num      int64 = 330 * neuron_num_coefs // how many PNs will receive stimulus
	stim_LN_num      int64 = 120 * neuron_num_coefs
	// ...
	ORN_number      int64   = 200
	stim_onset      float64 = 1.0 * float64(ms_per_second) // 1.5 stimulus starts at this moment ! in ms
	stim_offset     float64 = 3.5 * float64(ms_per_second) // 4.0 withdraw stimulus at this moment (time in ms)
	stim_rise       float64 = 0.4 * float64(ms_per_second) // 0.5 rise time of stimulus input onset (1.5-2)
	stim_pDecay     float64 = 3.0 * float64(ms_per_second) // 2.0 fade decay time (the real one is Inf)
	fading_rate     float64 = 0.99800                      // exp(-0.01/5)=0.998
	click_per_ms    int64   = 1                            // time steps (click/iteration) per ms
	click_num_total int64   = click_per_ms * time_len      // time steps (clicks) in total
	time_stepLen    float64 = 1.0 / float64(click_per_ms)  // each time step 0.01ms (corresponding to click_per_ms)
)

var (
	BG_input_rate         float64              = 0.0347107 // !!! using program val // 3.50000(paper)
	ORN_input_rate        float64              = 0.0003572 // !!! using program val // 0.03500(paper)
	BG_input_strength_PN  float64              = 0.06540
	BG_input_strength_LN  float64              = 0.00010
	ORN_input_strength_PN float64              = 0.01743
	ORN_input_strength_LN float64              = 0.01667
	PN_reactor            [PN_number][2]PNtype // PNs' last 2 states&currents structs
	LN_reactor            [LN_number][2]LNtype // LNs' last 2 states&currents structs
	CLOCK                 float64              = 0.0
	err                   error                = nil
)

type PNtype struct { //PN struct
	stim float64 // input stimulations
}

type LNtype struct { //LN struct
	stim float64 // input current
}

func get_stim_PN(id int64) {
	var inputRate, ret float64 = 0, fading_rate * PN_reactor[id][0].stim
	var clock float64 = float64(int64(math.Floor(CLOCK)) % time_len)
	var i int64 = 0
	// ...
	if rand.Float64() < (BG_input_rate * time_stepLen) {
		ret -= BG_input_strength_PN
	}
	if clock < stim_onset {
		inputRate = 0
	} else if clock >= stim_onset && clock < (stim_onset+stim_rise) { // rising stimulus
		inputRate = math.Exp(-math.Pow(clock-stim_onset-stim_rise, 2)/100000) * ORN_input_rate
	} else if clock >= (stim_onset+stim_rise) && clock < stim_offset { // normal stimulus
		inputRate = ORN_input_rate
	} else if clock >= stim_offset { // decay stimulus
		inputRate = math.Exp(-math.Sqrt(clock-stim_offset)/math.Sqrt(1000)) * ORN_input_rate
	}
	if id > stim_PN_num {
		return
	}
	for i = 0; i < ORN_number; i++ {
		if rand.Float64() < (inputRate * time_stepLen) {
			ret -= ORN_input_strength_PN
		}
	}
	PN_reactor[id][0].stim = ret
	fmt.Println(ret)
}

func main() {
	var click int64
	CLOCK = 0
	for click = 1; click <= click_num_total; click++ { // each time step is 0.01 ms
		CLOCK = CLOCK + time_stepLen
		get_stim_PN(0)
	}
}
