<template>
    <div class="jumbotron vertical-center">
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css" integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R" crossorigin="anonymous">
      <b><p>Welcome to Steven's Sudoku Solver</p></b>
      <hr><br>
      <SudokuGrid/>
      <hr><br>
      <div class="row">
        <div class="col-sm-12" align="center">
            <SolveBoard id="solve-button"/> 
            <ResetBoard id="reset-button"/>
        </div>
      </div>
    </div>
    </div>
</template>

<script>

import SolveBoard from './components/SolveBoard.vue';
import SudokuGrid from './components/SudokuGrid.vue';
import ResetBoard from './components/ResetBoard.vue';
export default {
  components: {
    SolveBoard,
    SudokuGrid,
    ResetBoard
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
