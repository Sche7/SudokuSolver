<template>
    <div class="card border-primary mb-3" style="max-width: 20rem;">
        <div class="card-header">{{ header }}</div>
        <div class="card-body">
            <h4 class="card-title">{{ title }}</h4>
            <p class="card-text">{{ cardText }}</p>
    </div>
</div>
</template>

<script>

export default {
    name: 'HoverCard',
    props: ['header', 'title', 'cardText']
}

</script>