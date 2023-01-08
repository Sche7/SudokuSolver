<template>
    <div>
        <fulfilling-bouncing-circle-spinner
            :animation-duration="4000"
            :size="25"
            :color="activeColor"
            v-if="computing"
        />
        <fulfilling-bouncing-circle-spinner
            :animation-duration="0"
            :size="25"
            :color="idleColor"
            v-else
        />
    </div>
</template>

<script>
import {FulfillingBouncingCircleSpinner} from 'epic-spinners';

export default {
    name: 'LoadingSpinner',
    components: {
        FulfillingBouncingCircleSpinner
    },
    data(){
        return {
            idleColor: '#2ca444',
            activeColor: '#ff1d5e',
        }
    },
    props: ['computing'],
}
</script>
