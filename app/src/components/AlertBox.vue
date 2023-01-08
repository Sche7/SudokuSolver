<template>
    <div style="width: 600px;margin-top: 50px;">
    <Transition>
        <div class="alert alert-dismissible alert-danger" v-if="error">{{ error }}</div>
        <div class="alert alert-dismissible alert-success" v-else-if="success">{{ success }}</div>
    </Transition>
    </div>
</template>

<script>

export default {
    name: 'AlertBox',
    props: ['error', 'success'],

}
</script>