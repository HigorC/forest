<template>
    <div id="app">
        <section id="sidebar-section">
            <b-sidebar
                    position="static"
                    :mobile="mobile"
                    :expand-on-hover="expandOnHover"
                    :reduce="reduce"
                    :fullheight=true
                    type="is-light"
                    open
            >
                <div class="p-1">
                    <div class="title block">
                        FOREST
                    </div>
                    <b-menu class="is-custom-mobile">
                        <b-menu-list label="Árvores">
                            <b-menu-item active label="AVL"></b-menu-item>
                            <b-menu-item label="Rubro-Negra"></b-menu-item>
                        </b-menu-list>
                    </b-menu>
                </div>
            </b-sidebar>
        </section>
    </div>
</template>

<script>
    export default {
        name: 'App',
        components: {}
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

    .p-1 {
        .title {
            font-family: 'Gotu', sans-serif;
        }
        padding: 1em;
    }

    @media screen and (max-width: 1023px) {
        .b-sidebar {
            .sidebar-content {
                &.is-mini-mobile {
                    &:not(.is-mini-expand),
                    &.is-mini-expand:not(:hover) {
                        .menu-list {
                            li {
                                a {
                                    span:nth-child(2) {
                                        display: none;
                                    }
                                }

                                ul {
                                    padding-left: 0;

                                    li {
                                        a {
                                            display: inline-block;
                                        }
                                    }
                                }
                            }
                        }

                        .menu-label:not(:last-child) {
                            margin-bottom: 0;
                        }
                    }
                }
            }
        }
    }

    @media screen and (min-width: 1024px) {
        .b-sidebar {
            .sidebar-content {
                &.is-mini {
                    &:not(.is-mini-expand),
                    &.is-mini-expand:not(:hover) {
                        .menu-list {
                            li {
                                a {
                                    span:nth-child(2) {
                                        display: none;
                                    }
                                }

                                ul {
                                    padding-left: 0;

                                    li {
                                        a {
                                            display: inline-block;
                                        }
                                    }
                                }
                            }
                        }

                        .menu-label:not(:last-child) {
                            margin-bottom: 0;
                        }
                    }
                }
            }
        }
    }
</style>
