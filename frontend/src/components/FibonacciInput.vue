<template>
   <div class="container">
     <div class="mainFibo_section">
       <!-- Header section -->
       <div class="header">
         <h2>Get N<sup>th</sup> Fibonacci Sequence Number</h2>
       </div>
       
       <!-- Input section -->
       <input v-model="number" type="number" placeholder="Enter a number">
       <button @click="getFibonacci">Get Number</button>
       
       <!-- Result section -->
       <div class="result">
         <textarea v-model="result" placeholder="The Nth sequence number is..."></textarea>
       </div>
     </div>
   </div>
 </template>
 
 
 <script>
 import axios from 'axios';
 
 export default {
   data() {
     return {
       number: null, // Holds the input number
       result: null, // Holds the result of the Fibonacci sequence
     };
   },
   methods: {
     async getFibonacci() {
      // Constructs the URL for the API request
       const url = 'http://localhost:8000/fibonacci/' + this.number; 
       await axios.get(url)
         .then(response => {
           console.log(response.data);
           // Stores the result in the 'result' variable
           this.result = response.data.fibonacci; 
         })
         .catch(error => {
           console.error(error);
         });
     },
   },
 };
 </script>
 
 <style scoped>
 input, button, textarea {
   font-size: 20px;
 }
 
 .mainFibo_section {
   margin-left: 100px;
   margin-right: 100px;
   box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
 }
 
 .result {
   padding: 20px;
 }
 
 .result textarea {
   width: 80%;
   height: 200px;
 }
 </style>