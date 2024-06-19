import React, { useState, useEffect } from "react";

const HelloThere = () => {
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      const user = await loadUser();
      setCurrentUser(user);
    };

    fetchUser();
  }, []);

  return (
    <div>
      {currentUser ? <p>Hello {currentUser.name}</p> : <p>Loading...</p>}
    </div>
  );
};

async function loadUser() {
  await new Promise((resolve) => setTimeout(resolve, 100));
  return { id: 1, name: "Bob" };
}

export default HelloThere;
