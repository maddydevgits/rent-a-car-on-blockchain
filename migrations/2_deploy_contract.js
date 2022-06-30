const rentcar = artifacts.require("rentcar");

module.exports = function (deployer) {
  deployer.deploy(rentcar);
};
