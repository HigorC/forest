const BASE_URL = 'http://localhost:5000';

const insert = (typeTree, actualTree, valueToInsert) => {
    fetch(
        `${BASE_URL}/insert/${valueToInsert}`,
        {
            method: 'POST',
            headers: new Headers({
                "Content-Type": "application/json",
            }),
            body: JSON.stringify(
                {
                    type: typeTree,
                    tree: actualTree
                })
        }).then(res => {
        return res.json();
    }).then(res => {
        console.log(res);
    })
};

const remove = () => {

};

export default {
    insert,
    remove
}
