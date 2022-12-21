<template>
    <div align="center">
      <table>
        <tbody>
        <tr v-for="(row, idx) in grid" :key="idx">
          <td v-for="(cell, idy) in row" :key="idy" 
          :class="{ locked: grid[idx][idy].locked, selected:grid[idx][idy].selected }"
          @click="setSelected(grid[idx][idy], idx, idy)"> {{ grid[idx][idy].toString() }} </td>
        </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
//   import { mapState } from 'vuex';
  
  export default {
    name: 'SudokuGrid',
    // computed: mapState([
    //   'grid'
    // ]),
    data() {
        return {
            grid: [
            [0, 0, 9, 0, 0, 0, 4, 6, 3],
            [0, 0, 6, 3, 4, 0, 5, 2, 9],
            [2, 3, 4, 5, 6, 9, 7, 1, 8],
            [0, 6, 7, 0, 0, 0, 3, 4, 1],
            [0, 4, 0, 0, 3, 0, 2, 9, 5],
            [0, 2, 0, 0, 0, 0, 6, 8, 0],
            [0, 0, 2, 0, 0, 1, 9, 3, 4],
            [4, 9, 3, 8, 2, 5, 1, 7, 6],
            [0, 7, 0, 4, 9, 3, 8, 5, 2],
            ]
        }
    },
    methods: {
      pickNumber(e) {
        let typed = parseInt(String.fromCharCode(e.keyCode),10);
        // if it was NaN, split out
        if(!typed) return;
        console.log(typed);
      },
      setSelected(cell,x,y) {
        console.log(cell)
        console.log(x)
        console.log(y)
      }
    },
    mounted() {
      window.addEventListener('keypress', this.pickNumber);
    },
    unmounted() {
      window.removeEventListener('keypress', this.pickNumber);
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
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
