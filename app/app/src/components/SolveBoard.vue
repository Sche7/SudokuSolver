<template>
    <div>
        <button @click="SolveBoard" type="button" class="btn btn-success btn-sm"> Solve board </button>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'SolveBoard',
    methods : {
        SolveBoard(){
            const path = 'http://localhost:5000/solve';
            axios.get(path)
            .then ((res) => {
                console.log(res.data)
                this.msg = res.data;
            })
            .catch((err) => {
                console.error(err)
            })
        }
    },
    created(){
        this.SolveBoard();
    }
}
</script>
