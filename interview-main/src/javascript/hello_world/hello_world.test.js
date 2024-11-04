const helloWorld = require("./hello_world");

describe("existance of functions:", () => {
    test("defined", () => {
        expect(helloWorld).toBeDefined();
    });

    test("is a function", () => {
        expect(typeof helloWorld).toEqual("function");
    });
});

describe("logic", () => {
    xtest("returns Hello, World!", () => {
        expect(helloWorld(0)).toBe("Hello, World!");
    });
});