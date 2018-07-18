function regularFunc() {
  console.log("I am a regular function");
}

regularFunc();

arrFunc = () => {
  console.log("I am a arrow function", this);
};

arrFunc();
