<template>
    <div>
        <!--        {{arrayInOrderTree}}-->
        <!--        <hr>-->
        <!--        {{treeInLevels}}-->
        <!--        <hr>-->
        <!--        <div v-for="(values) in treeInLevels" v-bind:key="values" class="level">-->
        <!--            <span v-for="node in values" v-bind:key="node" class="node" :class="{'empty-node': node === null }">-->
        <!--                {{node}}-->
        <!--            </span>-->
        <!--        </div>-->
        <button @click="teste">aa</button>
        <canvas id="treeCanvas">
        </canvas>
    </div>
</template>

<script>
    import api from '../scripts/api'

    export default {
        name: "TreeVisualizator",
        data: () => {
            return {
                treeInLevels: {},
                arrayInOrderTree: []
            }
        },
        methods: {
            teste: function () {
                this.treeInLevels = {
                    "1": [
                        8
                    ],
                    "2": [
                        4,
                        10
                    ],
                    "3": [
                        3,
                        5,
                        9,
                        11
                    ],
                    "4": [
                        1,
                        null,
                        null,
                        6,
                        null,
                        null,
                        null,
                        12
                    ],
                    "5": [
                        null,
                        null,
                        null,
                        null,
                        null,
                        null
                    ]
                };

                function makeCircle(x, y, radius) {
                    ctx.arc(x, y, radius, 0, 2 * Math.PI, false);
                    ctx.fillStyle = '#0dbd51';
                    ctx.fill();
                    ctx.lineWidth = 1;
                    ctx.strokeStyle = '#003300';
                    ctx.stroke();
                }

                const canvas = document.getElementById("treeCanvas");
                const ctx = canvas.getContext("2d");
                // Fix blur problem
                canvas.width = canvas.getBoundingClientRect().width;
                canvas.height = canvas.getBoundingClientRect().height;

                const centerX = canvas.width / 2;
                // const centerY = canvas.height / 2;
                const radius = 20;

                const heightToJump = radius + 10;

                for (let level in this.treeInLevels) {
                    // console.log(this.treeInLevels[level])
                    let actualCenterY = heightToJump;
                    this.treeInLevels[level].forEach(value => {
                        console.log(value)
                        makeCircle(centerX, actualCenterY, radius);
                        actualCenterY += radius * 2 + 10;
                    })
                }


                // makeCircle(centerX, centerY, radius);
                // makeCircle(330, 0, radius);


            }
        },
        mounted() {
            this.$root.$on('addOnTree', async (type, numberToInsert) => {
                if (type && numberToInsert) {
                    let result = await api.insert(type, this.arrayInOrderTree, numberToInsert);
                    console.log(result);
                    this.arrayInOrderTree = Object.assign([], result.arrayInOrderTree);
                    this.treeInLevels = Object.assign({}, result.treeInLevels);
                }
            })
        }
    }
</script>

<style lang="scss" scoped>
    #treeCanvas {
        border: 1px solid #000000;
        width: 65%;
        height: 90vh;
    }

    .level {
        margin: 10px 0;
        justify-content: center;

        .node {
            background-color: #0dbd51;
        }

        .empty-node {
            background-color: darkgrey;
        }

        .node, .empty-node {
            color: #ffffff;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 20px;
            margin-right: 10px;
        }

        .node:last-child {
            /*margin-right: 0;*/
        }
    }
</style>