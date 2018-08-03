package main

import "fmt"

func Sqrt(x float64) float64 {
  z := 1.0
  for i := 0; i<100;i++ {
    z -= (z*z - x)/ (z*2)
  }
  return z

}

func main() {
  fmt.Println(Sqrt(2))
}
