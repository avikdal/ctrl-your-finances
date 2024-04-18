import React, { useState, useEffect } from "react";
import { Chart } from "react-google-charts";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import InputAdornment from '@mui/material/InputAdornment';
import FormControl from '@mui/material/FormControl';
import Button from '@mui/material/Button';
import { AppContext } from '../context/Context'



// grab user data and have house account toggle for different access to goal charts

function Budgeting() {
    const [userGoals, setUserGoals] = useState([]);
    const [goalName, setGoalName] = useState("");
    const [savedMoney, setSavedMoney] = useState(0);
    const [targetAmount, setTargetAmount] = useState(0);
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
      // fetch user's goals from backend
      fetchUserGoals();
    },[])


    const { userId } = AppContext()


    const fetchUserGoals = async () => {
      try {
        // Make API call to fetch users goals
        const response = await fetch(`http://127.0.0.1:5555/api/goals/${userId.id}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          }
        });
        if (response.ok) {
          const data = await response.json()
          setUserGoals(data)
        } else {
          console.error("failed fetch error", error)
        }
      } catch (error){
        console.error("error fetching user goals:", error)
      }
    };




    //add new goals to user db
    const addGoal = async () => {
      try {
        // Make API call to users goals
        const response = await fetch(`http://127.0.0.1:5555/api/goals/${userId.id}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: goalName,
            saved: savedMoney,
            target: targetAmount
          })
        });
        if (response.ok) {
          const data = await response.json();
          console.log("added data", data)
          setGoalName("");
          setSavedMoney(0);
          setTargetAmount(0);
          fetchUserGoals();
        }else {
          console.error("Failed to add goal");
        }
      } catch (error) {
      console.error("Error adding goal:", error);
      }
    };

  
    const options = {
      title: "Your Financial Goals",
      legend: { position: "none" },
      colors: ["#009933"], 
    };


    const chartData = {
      old: [["Name", "Goal"]],
      new: [["Name", "Money Saved"]],
  };

  userGoals.forEach(goal => {
      chartData.old.push([goal.name, goal.target]);
      chartData.new.push([goal.name, goal.saved]);
  });


  

    return (
        <div>
          <Box
            sx={{
            padding: '20px', 
            border: '1px solid #ccc', 
            borderRadius: '5px',
            maxWidth: '500px',
            flexGrow: 1,
            margin: 'auto',
            marginTop: '20px' 
            }}
          >
            <h1 style={{fontFamily: 'Poppins', color: '#009933'}}>BUDGETING GOALS</h1>
            <h2 style={{ fontFamily: 'Poppins', color: '#32004C' }}>Set Your Financial Goals</h2>
            <p style={{ fontFamily: 'Poppins', color: '#32004C' }}>Start your journey towards financial well-being today. Define clear, achievable goals that align with your aspirations and values.</p>

            {!showForm && (
              <Button 
              variant="contained"
              size="large"
              style={{ backgroundColor: "#009933", marginTop: '10px' }}
              fullWidth
              onClick={() => setShowForm(true)}
              >
                Add Goal
              </Button>
            )}

            {showForm && (
            <form
              noValidate
              autoComplete="off"
              // onSubmit={handleSubmit}
              onSubmit={(e) => { e.preventDefault(); addGoal(); }}
              sx={{ display: 'block' }} // Set display to block to stack elements vertically
            >
              <TextField
                  label="What are you saving for"
                  fullWidth
                  id="outlined-start-adornment"
                  sx={{ m: 1, width: '100%', display: 'block' }} 
                  type="text"
                  value={goalName}
                  onChange={(e) => setGoalName(e.target.value)}
              />

              <FormControl sx={{ m: 1, width: '100%', display: 'block' }}> 
                  <InputLabel htmlFor="outlined-adornment-amount">Saved</InputLabel>
                  <OutlinedInput
                      id="outlined-adornment-amount"
                      startAdornment={<InputAdornment position="start">$</InputAdornment>}
                      label="Amount"
                      fullWidth
                      type="number"
                      value={savedMoney}
                      onChange={(e) => setSavedMoney(parseInt(e.target.value))}
                  />
              </FormControl>

              <FormControl sx={{ m: 1, width: '100%', display: 'block' }} > 
                  <InputLabel htmlFor="outlined-adornment-amount">Target</InputLabel>
                  <OutlinedInput
                      id="outlined-adornment-amount"
                      fullWidth
                      startAdornment={<InputAdornment position="start">$</InputAdornment>}
                      label="Amount"
                      type="number"
                      value={targetAmount}
                      onChange={(e) => setTargetAmount(parseInt(e.target.value))}
                  />
              </FormControl>
              
              <Button
                  type="submit"
                  variant="contained"
                  size="large"
                  style={{ backgroundColor: "#009933", marginTop: '10px' }}
                  fullWidth
              >
                  Add Goal
              </Button>
            </form>
             )}
          </Box>

          {userGoals ? 
          <Chart
              chartType="BarChart"
              width="100%"
              height="400px"
              diffdata={chartData}
              options={options}
          />
          : null}

        </div>
    )
}

export default Budgeting

