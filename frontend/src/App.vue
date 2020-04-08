<template>
<div id="app">
    <Menu></Menu>
</div>
</template>

<script>
    import Menu from "./components/Menu";

    export default {
        name: 'App',
        components: { Menu }
    }
</script>

<style scoped lang="scss">
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
</style>