const BASE_URL = 'http://localhost:5000';

const insert = (typeTree, actualTree, valueToInsert) => {
    return fetch(
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
    });
};

const remove = () => {

};

export default {
    insert,
    remove
}
