<!-- Foro -->
<!-- https://stackoverflow.com/questions/48241165/create-switch-for-changing-Theme-intead-of-browser-page-style-html#48241284 -->
<!-- https://stackoverflow.com/questions/8796107/how-to-make-changeable-Themes-using-css-and-javascript -->

<nav class="navbar bg-dark navbar-expand-lg bg-body-tertiary"
   <?php if ($_COOKIE["Theme"] == "darkly"): ?>
      data-bs-Theme="dark"
    <?php endif ?> >
    <div class="container-fluid">
      <a class="navbar-brand"
        href="./index.php">
        <img src="./static/img/logo.png"
          alt="Logo Aplication">
        ContactApp
      </a>
      <button class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse"
        id="navbarSupportedContent">
        <div class="d-flex justify-content-between w-100">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <?php if (isset($_SESSION["user"])): ?>
              <li class="nav-item">
                <a class="nav-link active"
                aria-current="page"
                href="./home.php">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link"
                href="./add.php">Add Contact</a>
              </li>

              <li class="nav-item">
                <a class="nav-link"
                href="./logout.php">Logout</a>
              </li>
              <?php else: ?>

              <li class="nav-item">
                <a class="nav-link active"
                  aria-current="page"
                  href="./register.php">Register</a>
              </li>
              <li class="nav-item">
                <a class="nav-link"
                  href="./login.php">Login</a>
              </li>
              <?php endif ?>
          </ul>
        </div>
        <?php if (isset($_SESSION["user"])): ?>
        <div class="p-4">
          <?= $_SESSION["user"]["email"]; ?>
        <?php endif ?>
        </div>
          <form action="<?= htmlspecialchars($_SERVER["PHP_SELF"]) ?>" method="post" class="d-flex gap-2">
            <button type="submit" name="Theme" value="flatly" class="btn btn-outline-success">Light</button>
            <button type="submit" name="Theme" value="darkly" class="btn btn-outline-info">Dark</button>
          </form>
      </div>
</nav>