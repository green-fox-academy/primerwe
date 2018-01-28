'use strict';
 
 let xhr = new XMLHttpRequest();
 
 xhr.onreadystatechange = function () {
     if (xhr.readyState === 4) {
         let content = JSON.parse(xhr.responseText);
         console.log(content.data.images.original.url);
         let gifHTML = '<img src=" ' + content.data.images.original.url + ' ">'; //: img HTML tag dinamikus megkonstruálása
         document.getElementById('ajax').innerHTML = gifHTML;
     }
 };
 
 xhr.open('GET', 'http://api.giphy.com/v1/gifs/translate?api_key=2NaHf0oqvaBflMtJ9Ya71Xm218wJ9do2&s=cat&limit=16&offset=0&rating=G&lang=en', true);
 
 xhr.send();