"use strict"; //strict mode
function convertToDec(num,base){
	//this converts a number of a given base to base-10
	let key = {};
	/* the following for loops create a conversion chart, in a
	sense, between base-10 numbers and their characters*/
	for(let i=0; i<10; i++){
		key[i.toString()] = i;
	}
	for(let i=10; i<36; i++){
		key[String.fromCharCode(i+87)] = i;
	}
	//split the number into before the decimal and after
	let parts = num.split(".");
	if(parts[0]){
		//if there are digits before decimal, convert them
		parts[0] = parseInt(parts[0],base);
	} else{
		parts[0] = 0;
	}
	if(parts[1]){
		//if there are digits after decimal, convert them
		let aftdec = 0;
		//iterate through each digit and add its converted value to aftdec
		for(let i=1; i<=parts[1].length; i++){
			let mult = parts[1][i-1];
			mult = key[mult];
			aftdec+=Math.pow(base,-i)*mult;
		}
		parts[1] = aftdec.toString();
	} else{
		parts[1] = 0;
	}
	//convert strings to floating points and add them
	num = parseFloat(parts[0])+parseFloat(parts[1]);
	return num;
}