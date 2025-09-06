import React, { useEffect, useState } from "react";
import axios from "axios";
import EmailItem from "./EmailItem";

export default function EmailList() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/emails/db")
      .then(res => setEmails(res.data.emails))
      .catch(err => console.log(err));
  }, []);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Emails</h1>
      {emails.map(email => (
        <EmailItem key={email.id} email={email} />
      ))}
    </div>
  );
}
