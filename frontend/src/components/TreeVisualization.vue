<template>
    <div>
        {{tree}}
    </div>
</template>

<script>
    import api from '../scripts/api'

    export default {
        name: "TreeVisualizator",
        data: () => {
            return {
                tree: []
            }
        },
        mounted() {
            this.$root.$on('addOnTree', async (type, numberToInsert) => {
                if (type && numberToInsert) {
                    let result = await api.insert(type, this.tree, numberToInsert);
                    console.log(result)
                    this.tree = Object.assign([], result.tree);
                }
            })
        }
    }
</script>

<style scoped>

</style>