class Player {
  constructor(img, xx, yy) {
    this.image = img;
    this.width = xx;
    this.height = yy;
    this.x = 0; this.xDiff = 0;
    this.y = 0; this.yDiff = 0;
    this.ms = 0;
  }
  // Position und Geschwindigkeit
  setPosition(x, y) {
    this.x = x; this.y = y;
  }
  setSpeed(dx, dy, ms) {
    this.xDiff = dx;
    this.yDiff = dy;
    this.ms = ms;
  }
  changePosition() {
    this.x += this.xDiff;
    this.y += this.yDiff;
  }
  changeDirection(LeftRight) {
    if (LeftRight) this.xDiff = -this.xDiff;
    else this.yDiff = -this.yDiff;
  }
  changeOrientation(orientation) {
    switch (orientation) {
      case 1 : this.x -= this.xDiff; break;
      case 2 : this.y -= this.yDiff; break;
      case 3 : this.x += this.xDiff; break;
      case 4 : this.y += this.yDiff;
    }
  }
  // Grenzkontrollen
  controlBorder(xL, xR, yT, yB) {
    if (this.x < xL || this.x > xR) this.xDiff = -this.xDiff;
    if (this.y < yT || this.y > yB) this.yDiff = -this.yDiff;
  }
  controlXBorder(xL, xR, yT, yB) {
    var orientation = 0;
    if (this.x < xL) { this.xDiff = -this.xDiff; orientation = 1; }
    if (this.y < yT) { this.yDiff = -this.yDiff; orientation = 2; }
    if (this.x > xR) { this.xDiff = -this.xDiff; orientation = 3; }
    if (this.y > yB) { this.yDiff = -this.yDiff; orientation = 4; }
    return orientation;
  }
  controlEdge(xL, xR, yT, yB) {
    if (this.x < xL) this.x = xR;
    if (this.y < yT) this.y = yB;
    if (this.x > xR) this.x = xL;
    if (this.y > yB) this.y = yT;
  }
  controlXEdge(xL, xR, yT, yB) {
    var edge = false;
    if (this.x < xL) { this.x = xR; edge = true; }
    if (this.y < yT) { this.y = yB; edge = true; }
    if (this.x > xR) { this.x = xL; edge = true; }
    if (this.y > yB) { this.y = yT; edge = true; }
    return edge;
  }

  // Hinderniskontrollen 
  controlContact(xL, xR, yT, yB) {
    if (this.x > xL-this.width  && this.x < xR
     && this.y > yT-this.height && this.y < yB) {
      this.xDiff = -this.xDiff;
      this.yDiff = -this.yDiff;
    }
  }
  controlXContact(xL, xR, yT, yB, mode) {
    if (this.x > xL-this.width  && this.x < xR
     && this.y > yT-this.height && this.y < yB) {
      // "Prall-Ausgleich"
      this.x -= this.xDiff; this.y -= this.yDiff;
      // zufällige Abweichungen
      var xx = 0; var yy = 0;  // mode == 0
      if (mode == 1 || mode == 3) 
        xx = Math.floor(Math.random()*8);
        //xx = Math.floor(Math.random()*16)-8;
      if (mode == 2 || mode == 3)
        yy = Math.floor(Math.random()*5);
        //yy = Math.floor(Math.random()*10)-5;
      this.xDiff = -this.xDiff + xx;
      this.yDiff = -this.yDiff + yy;
      // ggf. Korrektur
      if (this.xDiff > 15) this.xDiff = 10;
      if (this.xDiff < -15) this.xDiff = -10;
      if (this.yDiff > 10) this.yDiff = 5;
      if (this.yDiff < -10) this.yDiff = -5;
    }
  }
  isTouching(xL, xR, yT, yB) {
    if (this.x < xL || this.x > xR || this.y < yT || this.y > yB) return true;
    else return false;
  }
  isHitting(xL, yT) {
    if (this.x == xL && this.y == yT) return true;
    else return false;    
  }

  // Darstellung
  showImage() {
    context.drawImage(this.image, this.x, this.y, this.width, this.height); 
  }
}
