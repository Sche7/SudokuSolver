<template>
    <div>
        <button type="button" class="btn btn-success btn-sm"> {{ msg }}</button>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'Solve',
    data(){
        return {
            msg: ""
        }
    },
    methods : {
        getResponse(){
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
        this.getResponse();
    }
}

</script>