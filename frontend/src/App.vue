<template>
    <div id="app">
        <div class="menu-container">
            <Menu></Menu>
        </div>
        <div class="tree-container">
            <TreeVisualization></TreeVisualization>
        </div>
    </div>
</template>

<script>
    import Menu from "./components/Menu";
    import TreeVisualization from "./components/TreeVisualization";

    export default {
        name: 'App',
        components: {Menu, TreeVisualization}

    }
</script>

<style scoped lang="scss">
    .menu-container {
        max-width: 30%;
        height: 100%;
        float: left;
    }

    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
</style>