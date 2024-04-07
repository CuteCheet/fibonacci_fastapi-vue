<template>
 <div class="container">
   <div class="mainFibo_section">
      <div class="header">
         <h2>Get N<sup>th</sup> Fibonacci Sequence Number</h2>
      </div>
      <input v-model="number" type="number" placeholder="Enter a number">
      <button @click="getFibonacci">Get Number</button>
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
      number: null,
      result: null,
    };
 },
 methods: {
    async getFibonacci() {
      const url = 'http://localhost:8000/fibonacci/' + this.number;
      axios.get(url)
      .then(response => {
        console.log(response.data);
        this.result = response.data.fibonacci
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