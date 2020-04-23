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
        <button @click="printTree">aa</button>
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
            printTree: function () {
                // this.treeInLevels = {
                //     "1": [
                //         8
                //     ],
                //     "2": [
                //         4,
                //         10
                //     ],
                //     "3": [
                //         3,
                //         5,
                //         9,
                //         11
                //     ],
                //     "4": [
                //         null,
                //         null,
                //         null,
                //         null,
                //         null,
                //         null,
                //         null,
                //         null
                //     ]
                // };

                function makeCircleWithText(x, y, radius, text) {
                    ctx.beginPath();
                    ctx.fillStyle = '#0dbd51';
                    ctx.arc(x, y, radius, 0, 2 * Math.PI, false);

                    ctx.lineWidth = 1;
                    ctx.strokeStyle = '#003300';
                    ctx.stroke();

                    ctx.fill();

                    //Text
                    ctx.beginPath();
                    ctx.font = "20px Arial";
                    ctx.textAlign = 'center';
                    ctx.fillStyle = "white";
                    ctx.fillText(text, x, y + 5);
                    ctx.fill();
                }

                const canvas = document.getElementById("treeCanvas");
                const ctx = canvas.getContext("2d");
                ctx.font = "30px Arial";
                // Fix blur problem
                canvas.width = canvas.getBoundingClientRect().width;
                canvas.height = canvas.getBoundingClientRect().height;

                const radius = 25;

                const heightToJump = radius * 2;
                const centerX = canvas.width / 2;

                let actualCenterY = heightToJump;

                for (let level in this.treeInLevels) {
                    let actualCenterX = centerX / this.treeInLevels[level].length;
                    const localWithToJump = actualCenterX;
                    const that = this;
                    let hasPassedHalf = false;
                    this.treeInLevels[level].forEach((value, index) => {
                        if (that.treeInLevels[level].length > 1 && !hasPassedHalf && index + 1 > that.treeInLevels[level].length / 2) {
                            actualCenterX = centerX + localWithToJump;
                            hasPassedHalf = true;
                        }

                        if (value) {
                            if (that.treeInLevels[level].length > 1) {
                                ctx.beginPath();
                                ctx.moveTo(actualCenterX, actualCenterY - radius);

                                if (index % 2 === 0) {
                                    ctx.lineTo(actualCenterX + localWithToJump, actualCenterY - heightToJump);
                                } else {
                                    ctx.lineTo(actualCenterX - localWithToJump, actualCenterY - heightToJump);
                                }

                                ctx.stroke();
                            }

                            makeCircleWithText(actualCenterX, actualCenterY, radius, value);
                        }
                        actualCenterX = actualCenterX + (localWithToJump * 2);
                    });
                    actualCenterY += radius * 3;
                }
            }
        },
        mounted() {
            this.$root.$on('addOnTree', async (type, numberToInsert) => {
                if (type && numberToInsert) {
                    let result = await api.insert(type, this.arrayInOrderTree, numberToInsert);
                    console.log(result);
                    this.arrayInOrderTree = Object.assign([], result.arrayInOrderTree);
                    this.treeInLevels = Object.assign({}, result.treeInLevels);
                    this.printTree();
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