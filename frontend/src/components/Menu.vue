<template>
    <section id="sidebar-section">
        <b-sidebar
                position="static"
                :mobile="mobile"
                :expand-on-hover="expandOnHover"
                :reduce="reduce"
                :fullheight=true
                type="is-light"
                open>
            <div class="p-1">
                <div class="title block">
                    FOREST
                </div>
                <b-menu class="is-custom-mobile">
                    <b-menu-list label="Árvores">
                        <b-menu-item active label="AVL"></b-menu-item>
                        <b-menu-item label="Rubro-Negra"></b-menu-item>
                    </b-menu-list>
                    <hr>
                    <b-menu-list label="Operações">
                        <b-field>
                            <b-input placeholder="Número a inserir"
                                     type="search">
                            </b-input>
                            <p class="control">
                                <button class="button is-primary" @click="inserir">Inserir</button>
                            </p>
                        </b-field>
                    </b-menu-list>
                </b-menu>
            </div>
        </b-sidebar>
    </section>
</template>

<script>
    import api from '../scripts/api'
    export default {
        name: 'Menu',
        methods: {
            inserir: () => {
                console.log('oi')
                api.insert('avl', [1,2,3], 4)
            }
        }
    }
</script>

<style scoped lang="scss">
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
