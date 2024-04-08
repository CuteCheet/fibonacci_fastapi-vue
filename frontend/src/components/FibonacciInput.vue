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
 export default {
  data() {
     return {
       number: null, // Holds the input number
       result: null, // Holds the result of the Fibonacci sequence
     };
  },
  methods: {
     // Asynchronous method to fetch the Fibonacci sequence number
     async getFibonacci() {
       // Check if the input number is negative int
        if(this.number <= 0)
        {
          this.result = "Input number greater than 0";
        }
       // Check if the input number is acceptable
       else {
         // Construct the URL for the API request
         const url = 'http://localhost:8000/fibonacci/' + this.number;
         // Fetch the data from the backend
         const response = await fetch(url);
         // Parse the response as JSON
         const data = await response.json();
         // Update the result with the fetched Fibonacci number
         this.result = data.fibonacci;
       }
     },
  },
 };
 </script>
 
 <style scoped>
 /* Style the input, button, and textarea elements */
 input, button, textarea {
  font-size: 20px;
 }
 
 /* Style the main section */
 .mainFibo_section {
  margin-left: 100px;
  margin-right: 100px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
 }
 
 /* Style the result section */
 .result {
  padding: 20px;
 }
 
 /* Style the textarea within the result section */
 .result textarea {
  width: 80%;
  height: 200px;
 }
 </style>
 