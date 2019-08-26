package goStandard

import "testing"

func TestGoStandard(t *testing.T) {
	result1 := UncoveredIf(true)
	if result1 {
		t.Error("Failed UncoveredIf test")
	}

	result2 := FullyCovered()
	if !result2 {
		t.Error("Failed FullyCovered test")
	}
}
