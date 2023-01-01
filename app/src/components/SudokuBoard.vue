<template>
    <div align="center">
      <table>
        <tbody>
        <tr v-for="(row, idx) in grid" :key="idx">
          <td v-for="(cell, idy) in row" :key="idy" @click="setSelected(grid[idx][idy], idx, idy)">
            {{ greaterThanZero(grid[idx][idy]) }}
          </td>
        </tr>
        </tbody>
      </table>
      <div align="center" style="margin-top:10px">
          <div class="btn-group me-2" role="group">
            <button type="button" class="btn btn-secondary" @click="setNumber(1)">1</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(2)">2</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(3)">3</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(4)">4</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(5)">5</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(6)">6</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(7)">7</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(8)">8</button>
            <button type="button" class="btn btn-secondary" @click="setNumber(9)">9</button>
          </div>
      </div>
      <hr><br>
      <div class="sudokurow">
        <div>
            <button @click="randomizeBoard" class="btn btn-primary btn-sm" style="block-size:50px;margin-right: 10px;"> New puzzle </button>
            <button @click="solveBoard" class="btn btn-success btn-sm" style="block-size:50px;"> Solve puzzle </button>
        </div>
        <div style="margin-top:25px">
            <button @click="resetBoard" class="btn btn-outline-info" style="margin-right:10px;"> Reset puzzle </button>
            <button @click="cleanBoard" class="btn btn-outline-danger"> Clean board </button>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

const initial_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

export default {
    name: 'SudokuBoard',
    data() {
      return {
        grid: initial_grid,
        initial_grid: initial_grid,
        selected: [0, 0]
      }
    },
    methods : {
        solveBoard(){
          const path = 'http://localhost:5000/solve';
          axios.post(path, {data: this.grid})
          .then ((res) => {
            const result = res.data;
            Object.assign(this.$data, {grid: result});
          })
          .catch((err) => {
            console.error(err);
          })
        },
        randomizeBoard(){
          const path = 'http://localhost:5000/randomize';
          axios.get(path)
          .then ((res) => {
            const result = res.data;
            Object.assign(this.$data, {grid: result, initial_grid: result});
          })
          .catch((err) => {
            console.error(err);
          })
        },
        pickNumber(e) {
          let typed = parseInt(String.fromCharCode(e.keyCode), 10);
          // if it was NaN, split out
          if(!typed) return;
          console.log(typed);
        },
        setSelected(cell, x, y) {
          this.selected = [x , y]
        },
        setNumber(number) {
          const x = this.selected[0]
          const y = this.selected[1]
          this.grid[x][y] = number
        }
        ,
        greaterThanZero(cell){
          if (cell > 0) {
              return cell.toString();
          } else {
              return ""
          }
        },
        resetBoard(){
          console.log('Resetting...');
          Object.assign(this.$data, {grid: this.initial_grid});
          },
        cleanBoard(){
          console.log('Cleaning...');
          Object.assign(this.$data, {grid: initial_grid});
        }
    }
}
</script>

<style scoped>
table {
  border-collapse: collapse;
  border: 2px solid;
}

td {
  border: 1px solid;
  text-align: center;
  height: 40px;
  width: 40px;
}

table tbody tr td:nth-child(3), table tbody tr td:nth-child(6) {
  border-right: 2px solid;
}

table tbody tr:nth-child(3), table tbody tr:nth-child(6) {
  border-bottom: 2px solid;
}

td.locked {
  cursor: not-allowed;
}

td {
  cursor: pointer;
}

td.selected {
  background-color: bisque;
}

.sudokurow {
  display: inline;
}
</style>
