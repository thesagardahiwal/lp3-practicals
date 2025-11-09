// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure to store student information
    struct Student {
        uint id;
        string name;
        uint age;
        string course;
    }

    // Array to store all students
    Student[] public students;

    // Event to log new student addition
    event StudentAdded(uint id, string name);

    // Add a new student
    function addStudent(uint _id, string memory _name, uint _age, string memory _course) public {
        students.push(Student(_id, _name, _age, _course));
        emit StudentAdded(_id, _name);
    }

    // Get number of students
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Get student details by index
    function getStudent(uint index) public view returns (uint, string memory, uint, string memory) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.id, s.name, s.age, s.course);
    }

    // Fallback function to accept ETH
    fallback() external payable {
        // Accept ETH sent to contract
    }

    // Function to check contract balance
    function getContractBalance() public view returns (uint) {
        return address(this).balance;
    }
}
