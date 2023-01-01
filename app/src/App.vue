<template>
    <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      >
      <b><p>Welcome to Steven's Sudoku Solver</p></b>
      <hr><br>
        <SudokuBoard/>
    </div>
    </div>
</template>

<script>

import SudokuBoard from './components/SudokuBoard.vue';
export default {
  components: {
    SudokuBoard
}

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#solve-button {
  display:inline-block;
  margin-right: 15px;
}

#reset-button {
  display:inline-block;
  margin-right: 15px;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}
</style>
