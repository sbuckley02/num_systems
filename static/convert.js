"use strict";
function convertToDec(num,base){
	let key = {};
	for(let i=0; i<10; i++){
		key[i.toString()] = i;
	}
	for(let i=10; i<36; i++){
		key[String.fromCharCode(i+87)] = i;
	}
	let parts = num.split(".");
	if(parts[0]){
		parts[0] = parseInt(parts[0],base);
	} else{
		parts[0] = 0;
	}
	if(parts[1]){
		let aftdec = 0;
		for(let i=1; i<=parts[1].length; i++){
			let mult = parts[1][i-1];
			mult = key[mult];
			aftdec+=Math.pow(base,-i)*mult;
		}
		parts[1] = aftdec.toString();
	} else{
		parts[1] = 0;
	}
	num = parseFloat(parts[0])+parseFloat(parts[1]);
	return num;
}