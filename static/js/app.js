const footer = () => {
  const date = new Date();
  const thisYear = date.getFullYear();

  document.getElementById("copyright").innerHTML =
    "&copy; Copyright " + thisYear;
};

footer();
