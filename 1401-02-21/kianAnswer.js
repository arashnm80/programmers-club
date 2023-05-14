 let s = prompt('start')
 let d = prompt('end')
 let n = prompt('column')

function upAndRight(p, n) {
  let shift = 0;
  let r = 0;
  let u = 1;
  let layers = n;
  let C = 0;
  let endOfLayers
  for (let x = 0; true; x++) {
    endOfLayers = 4 * (layers - 1);
    C += endOfLayers;
    if (p <= C) {
      break;
    }
    layers -= 2;
  }
  let surpass = endOfLayers - (C - p);
  for (let x = 1; x <= surpass; x++) {
    if (x <= layers) {
      r += 1;
    } else if (x <= 2 * layers - 1) {
      u += 1;
    } else if (x <= 3 * layers - 2) {
      r -= 1;
    } else {
      u -= 1;
    }
  }
  shift = (n - layers) / 2;
   let result = [r + shift, u + shift];
   return result
}
// upAndRight(s, n) 
// upAndRight(d, n)
s_ru = upAndRight(s, n);
d_ru = upAndRight(d, n);
let rDiff = d_ru[0] - s_ru[0];
let uDiff = d_ru[1] - s_ru[1];
console.log(rDiff,uDiff);
