/*let anagram = (s1, s2) =>
  s1.split('').sort().join('') === s2.split('').sort().join('')*/


let anagram = function(string1, string2) {
  if (typeof string1 !== 'string') {
    throw new Error ('string1 is not a string!');
  } else if (typeof string2 !== 'string') {
    throw new Error ('string2 is not a string!');
  }
  
  let str1 = string1.toLowerCase().replace(/[^a-z\d]/g, '').split('').sort('').join('');
  let str2 = string2.toLowerCase().replace(/[^a-z\d]/g, '').split('').sort('').join('');
  
  if (str1.length !== str2.length) {
    throw new Error ('The two string are not an anagram!');
  } else if (str1 === str2) {
    return true;
  }
}

module.exports = anagram;

//console.log(anagram(123, 231));
