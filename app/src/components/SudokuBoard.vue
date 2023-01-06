<template>
    <div align="center">
      <div style="display:inline-flex;">
        <div style="block-size:25px;margin-right: 50px;">
          <div style="margin-bottom: 10px;margin-top: 10px;">
            <button @click="randomizeBoard" class="btn btn-primary btn-sm">New puzzle</button>
          </div>
          <div style="margin-top: 220px;">
            <button @click="validateBoard" class="btn btn-warning btn-sm">Validate puzzle</button>
          </div>
          <div style="margin-bottom: 10px;margin-top: 10px;">
            <button @click="solveBoard" class="btn btn-success btn-sm">Solve puzzle</button>
          </div>
        </div>

        <div>
          <table>
            <tbody>
            <tr v-for="(row, idx) in grid" :key="idx">
              <td
                v-for="(cell, idy) in row" :key="idy"
                @click="setSelected(idx, idy)"
                :style="[selected[0] == idx && selected[1] == idy ? {'background-color':'#cccccc'} : {}]"
              >
                {{ greaterThanZero(grid[idx][idy]) }}
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div align="center" style="margin-top: 10px;">
          <div class="btn-group" role="group">
            <button type="button" class="btn btn-secondary" @click="setNumber(0)">Blank</button>
            <button type="button" class="btn btn-secondary" v-for="number in 9" :key="number" @click="setNumber(number)">
              {{number}}
            </button>
          </div>
          <div style="margin-left:25px;display: inline;">
            <button type="button" class="btn btn-outline-success" @click="saveBoardState">Save</button>
            <button type="button" class="btn btn-outline-info" style="margin-left:10px;" @click="loadBoard">Load</button>
            <button type="button" class="btn btn-outline-secondary" style="margin-left:10px;" @click="cleanBoard" >Clear</button>
          </div>
      </div>
      <hr><br>
      <div class="alert alert-danger" v-if="error">
        {{ error }}
      </div>
      <div class="alert alert-success" v-else-if="success">
        {{ success }}
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
        grid: JSON.parse(JSON.stringify(initial_grid)),
        saved_grid: initial_grid,
        selected: [null, null],
        error: null,
        success: null
      }
    },
    methods : {
        solveBoard(){
          const path = 'http://localhost:5000/solve';
          axios.post(path, {data: this.grid})
          .then ((res) => {
            const result = res.data.solution;
            if(result.length == 0){
              Object.assign(this.$data, {
                error: 'Solution does not exist.',
                success: null
              })
            } else {
              Object.assign(this.$data, {
                grid: result,
                error: null,
                success: 'Solution found!'
              })
            }
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
            Object.assign(this.$data, {grid: result.puzzle, error: null, success: null});
          })
          .catch((err) => {
            console.error(err);
          })
        },
        validateBoard(){
          const path = 'http://localhost:5000/validate';
          axios.post(path, {data: this.grid})
          .then ((res) => {
            const result = res.data;
            if(!result.valid){
              Object.assign(this.$data, {error: 'Board is invalid.', success: null})
            } else {
              Object.assign(this.$data, {error: null, success: 'Board is valid!'})
            }
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
        setSelected(x, y) {
          this.selected = [x , y]
        },
        setNumber(number) {
          const x = this.selected[0]
          const y = this.selected[1]
          let grid_copy = JSON.parse(JSON.stringify(this.grid))
          grid_copy[x][y] = number
          Object.assign(this.$data, {grid: grid_copy})
        }
        ,
        greaterThanZero(cell){
          if (cell > 0) {
              return cell.toString();
          } else {
              return ""
          }
        },
        loadBoard(){
          console.log('Resetting board...');
          Object.assign(this.$data, {
            grid: this.saved_grid,
            error: null, 
            success: 'Successfully loaded board!'
          })
          },
        cleanBoard(){
          console.log('Cleaning board...');
          Object.assign(this.$data, {
            grid:
            initial_grid,
            error: null,
            success: 'Successfully cleaned board!'
          });
        },
        saveBoardState() {
          console.log('Saving board state...');
          Object.assign(this.$data, {
            saved_grid: this.grid,
            success: 'Successfully saved board!',
            error: null
          });
        },
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

</style>
