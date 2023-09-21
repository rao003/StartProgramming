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
  changeOrientation(orientation) {
    switch (orientation) {
      case 1 : this.x -= this.xDiff; break;
      case 2 : this.y -= this.yDiff; break;
      case 3 : this.x += this.xDiff; break;
      case 4 : this.y += this.yDiff;
    }
  }
  // Kollisionskontrollen
  controlBorder(xL, xR, yT, yB) {
    if (this.x < xL || this.x > xR) this.xDiff = -this.xDiff;
    if (this.y < yT || this.y > yB) this.yDiff = -this.yDiff;
  }
  controlEdge(xL, xR, yT, yB) {
    if (this.x < xL) this.x = xR;
    if (this.y < yT) this.y = yB;
    if (this.x > xR) this.x = xL;
    if (this.y > yB) this.y = yT;
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
