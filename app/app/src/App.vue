<template>
    <div class="jumbotron vertical-center">
    <div class="container">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css" integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R" crossorigin="anonymous">
      <b><p>Welcome to Steven's Sudoku Solver</p></b>
      <hr><br>
      <div class="row">
        <div class="col-sm-12" align="left">
            <button type="button" class="btn btn-success btn-sm">
              Solve board
            </button>
            <button type="button" class="btn btn-info btn-sm">
              Upload board
            </button>
            <button type="button" class="btn btn-primary btn-sm">
              Reset
            </button>
        </div>
      </div>
    </div>
    </div>
</template>

<script>

export default {

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
</style>
