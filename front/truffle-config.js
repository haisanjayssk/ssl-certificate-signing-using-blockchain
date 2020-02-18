const path = require("path");

// module.exports = {
//   // See <http://truffleframework.com/docs/advanced/configuration>
//   // to customize your Truffle configuration!
//   contracts_build_directory: path.join(__dirname, "client/src/contracts"),
//   networks: {
//     develop: {
//       port: 8545
//     }
//   }
// };

module.exports = {
  // See <http://truffleframework.com/docs/advanced/configuration>
  // to customize your Truffle configuration!
  // contracts_build_directory: path.join(__dirname, "client/src/contracts"),
  networks: {
    development: {
      host: "127.0.0.1",
      port: 9545,
      // from:'0x5aeda56215b167893e80b4fe645ba6d5bab767de',
      network_id: '*', // Match any network id
      gas:500000,
      websockets: true,  
    },
  },
 compilers: {
   solc:{
     version: '0.4.21'
   }
 }
};