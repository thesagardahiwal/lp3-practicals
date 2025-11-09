// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Bank {
    mapping(address => uint) private balances; // store balances per customer

    // Deposit money into the bank
    function deposit() public payable {
        require(msg.value > 0, "Deposit must be greater than 0");
        balances[msg.sender] += msg.value;
    }

    // Withdraw money from the bank
    function withdraw(uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Show the balance of the customer
    function getBalance() public view returns (uint) {
        return balances[msg.sender];
    }
}
