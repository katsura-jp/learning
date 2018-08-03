package main

import (
  "fmt"
  "os"
)

func main() {
  s := "hello"
  if s[1] != 'e' {
    os.Exit(1)
  }
  s = "good bye"

  var p *string = &s 
  *p = "ciao"
  //s[0] = 'x' (これは、エラー)
  //(*p)[1] = 'y' (これもエラー)
  fmt.Printf(s)
  fmt.Printf("\n")
  //var arrayOfInt [10]int
  si := sum([]int{1,2,3})
  fmt.Printf("%d",si)
  fmt.Printf("\n")
  m := map[string]int{"one":1,"twe":2}
  fmt.Println(m)

}

func sum(a []int) int {
  s := 0
  for i:= 0 ; i < len(a) ; i++ {
    s += a[i]
  }
  return s
}
