// SPDX-License-Identifier: MIT
pragma experimental ABIEncoderV2;
pragma solidity >=0.4.22 <0.9.0;

contract rentcar {
  
  address[] _users;
  string[] _pickups;
  string[] _dropoffs;
  string[] _pickupdates;
  string[] _dropoffdates;
  string[] _pickuptime;
  string[] _cartypes;
  string[] _phonenos;
  string[] _emailids;

  function addRequest(address user,string memory pickup,string memory dropoff,string memory pickupdate,string memory dropoffdate,string memory pickuptime,string memory cartype, string memory phoneno,string memory email) public {

    _users.push(user);
    _pickups.push(pickup);
    _dropoffs.push(dropoff);
    _pickupdates.push(pickupdate);
    _dropoffdates.push(dropoffdate);
    _pickuptime.push(pickuptime);
    _cartypes.push(cartype);
    _phonenos.push(phoneno);
    _emailids.push(email);

  }

  function viewRequests() public view returns(address[] memory,string[] memory,string[] memory,string[] memory,string[] memory,string[] memory,string[] memory,string[] memory,string[] memory) {
    return (_users,_pickups,_dropoffs,_pickupdates,_dropoffdates,_pickuptime,_cartypes,_phonenos,_emailids);
  }
}
