<!doctype html>
<html lang="pl">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Platforma Konkursowa GovTech">
    <meta name="author" content="hostlab.pl">
    <link rel="icon" type="image/ico" sizes="16x16" href="<?php echo base_url('assets/images/favicon.ico')?>">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i&amp;subset=latin-ext" rel="stylesheet">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="theme-color" content="#ffffff">

    <title>GovTech - Zaloguj się</title>

    <link href="<?php echo site_url('assets/css/bootstrap.min.css')?>" rel="stylesheet">
    <link href="<?php echo site_url('assets/css/signin.css')?>" rel="stylesheet">

    <script src="<?php echo site_url('assets/js/jquery-3.3.1.min.js')?>"></script>
    <script src="<?php echo site_url('assets/js/vendor/popper.min.js')?>"></script>
    <script src="<?php echo site_url('assets/js/bootstrap.min.js')?>"></script>
    <script src="<?php echo site_url('assets/js/vendor/holder.min.js')?>"></script>
    <script src="<?php echo site_url('assets/js/js.cookie.js')?>"></script>
    <script src="<?php echo site_url('assets/js/script.js')?>"></script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KSQK3DB');</script>
<!-- End Google Tag Manager -->
<!-- Hotjar Tracking Code for https://konkursy.govtech.gov.pl -->
<script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:1470096,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script>
  </head>

  <body class="text-center">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KSQK3DB"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
  <div class="container-fluid">
      <?php /* ?>
      <div class="row justify-content-right">
        <div class="col-md-12 text-center">
<a href="#" class="changeThemeColour changeLink"><span data-feather="eye"></span> Wersja dla słabo widzących</a>
 &nbsp; <a href="#" class="changeFontSize changeLink"><span data-feather="zoom-in"></span> Powiększ tekst</a>
        </div>
      </div>
      <?php */ ?>
    <div class="row header-logo">
      <div class="col-md-8 offset-md-2 my-5 text-left">
        <div class="h2"><strong>Platforma GovTech</strong></div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-8 offset-md-2 mt-2 text-left">

      <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item" style="margin-top: -2px;"><a href="https://govtech.gov.pl"><span data-feather="home"></span></a></li>
          <li class="breadcrumb-item"><a href="<?php echo base_url()?>">Platforma GovTech</a></li>
          <li class="breadcrumb-item active" aria-current="page">Logowanie</li>
        </ol>
      </nav>

      </div>
    </div>
    <div class="row">
      <div class="col-md-8 offset-md-2 my-2 text-left">
        <div class="h3 mb-4"><strong>Zaloguj się na Plaformę GovTech</strong></div>
<?php if($_counter>7 || $_login_failure_count>7){ ?>
<script type="text/javascript">
 var RecaptchaOptions = {
    theme : 'clean'
 };
</script>
<?php } ?>
<?php
$attributes = array('class'=>'form-signin');
echo form_open(site_url('login'),$attributes);

//<img class="mb-4 pb-5" src="< ?php echo site_url('assets/images/logo_govtech_pl.png')? >" alt="GovTech" style="max-width:275px;">

?>

<?php
echo $info_msg;
?>


      <?php echo form_error('user_email'); ?>
      <label for="inputEmail" >Adres email</label>
      <input type="email" id="inputEmail" class="form-control" placeholder="Adres email" name="user_email" required autofocus>
      <?php echo form_error('user_password'); ?>
      <label for="inputPassword" class="mt-2">Hasło</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Hasło" name="user_password" required>
<?php if($_counter>7 || $_login_failure_count>7){ ?>
      <div class="mb-3">
        <label for="recaptcha-field" class="mt-2">Kod zabezpieczający</label>
        <?php echo form_error('g-recaptcha-response'); ?>

<script>
    var onloadCallback = function () {
        grecaptcha.render('recaptcha-field', {'sitekey' : '<?php echo $siteKey ?>'});
    };
</script>
<div id="recaptcha-field" class="g-recaptcha"></div>

      </div>
<?php } ?>
      <div class="links text-left mb-5">
      <a href="<?php echo site_url('haslo')?>" >Odzyskaj hasło</a>
      </div>
      <div class="row">
        <div class="col-md-6 align-middle">
        <a class="btn-link btn-block mt-1" href="<?php echo site_url('rejestracja')?>" >Zarejestruj się</a>
        </div>
        <div class="col-md-6">
        <button class="btn btn-primary btn-block" type="submit">Zaloguj się</button>
        </div>
      </div>
    </form>
<?php if($_counter>7 || $_login_failure_count>7){ ?>
<script src="https://www.google.com/recaptcha/api.js?onload=onloadCallback&render=explicit" async defer></script>
<?php } ?>
      </div>
    </div>


<?php echo $this->load->view('stopka_niezalogowany_view', array(), true);	  ?>

  </div>
    <!-- Icons -->
    <script src="<?php echo site_url('assets/js/feather.js')?>"></script>
    <script>
      feather.replace()
    </script>

<!-- Ybug code -->
<script type='text/javascript'>
(function() {
    window.ybug_settings = {"id":"nvghw151zs"};
    var ybug = document.createElement('script'); ybug.type = 'text/javascript'; ybug.async = true;
    ybug.src = 'https://ybug.io/api/v1/button/'+window.ybug_settings.id+'.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ybug, s);
})();
</script>
<!-- Ybug code end -->
  </body>
</html>
