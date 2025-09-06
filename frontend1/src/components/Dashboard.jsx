import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  PieChart, Pie, Cell, Legend, Tooltip,
  BarChart, Bar, XAxis, YAxis, ResponsiveContainer
} from "recharts";

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042"];

export default function Dashboard() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/emails/db")
      .then(res => setEmails(res.data.emails))
      .catch(err => console.log(err));
  }, []);

  // Compute stats
  const totalEmails = emails.length;
  const resolvedEmails = emails.filter(e => e.status === "resolved").length;
  const pendingEmails = totalEmails - resolvedEmails;

  // Sentiment distribution
  const sentimentData = [
    { name: "Positive", value: emails.filter(e => e.sentiment === "Positive").length },
    { name: "Negative", value: emails.filter(e => e.sentiment === "Negative").length },
    { name: "Neutral", value: emails.filter(e => e.sentiment === "Neutral").length },
  ];

  // Priority distribution
  const priorityData = [
    { name: "Urgent", value: emails.filter(e => e.priority === "Urgent").length },
    { name: "Not Urgent", value: emails.filter(e => e.priority === "Not urgent").length },
  ];

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        <div className="bg-white shadow-md rounded-md p-4 text-center">
          <h2 className="font-bold text-lg">Total Emails</h2>
          <p className="text-2xl">{totalEmails}</p>
        </div>
        <div className="bg-white shadow-md rounded-md p-4 text-center">
          <h2 className="font-bold text-lg">Resolved Emails</h2>
          <p className="text-2xl text-green-600">{resolvedEmails}</p>
        </div>
        <div className="bg-white shadow-md rounded-md p-4 text-center">
          <h2 className="font-bold text-lg">Pending Emails</h2>
          <p className="text-2xl text-red-600">{pendingEmails}</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Sentiment Pie Chart */}
        <div className="bg-white shadow-md rounded-md p-4">
          <h2 className="font-bold text-lg mb-4">Sentiment Distribution</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={sentimentData}
                dataKey="value"
                nameKey="name"
                outerRadius={100}
                fill="#8884d8"
                label
              >
                {sentimentData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Priority Bar Chart */}
        <div className="bg-white shadow-md rounded-md p-4">
          <h2 className="font-bold text-lg mb-4">Priority Breakdown</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={priorityData}>
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="value" fill="#00C49F" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
