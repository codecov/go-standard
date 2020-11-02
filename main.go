package goStandard

// I'm a comment!

func UncoveredIf(a bool) bool {
	if a {
		return false
	}
	// I'm also a comment
	return true
}


func FullyCovered() bool {
	return true
}
/* Comment 3
* space
*/

func Uncovered() bool {
	return true
}
