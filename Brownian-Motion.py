import cv2
import time 
import numpy as np 

cap = cv2.VideoCapture('C:\\Users\\bilol\\Desktop\\Opencv Project\\Brownian-Motion.mp4')
starting_frame = 350
ending_frame = 475
current_frame = starting_frame

cap.set(cv2.CAP_PROP_POS_FRAMES,starting_frame)

active_pollens = {}
last_id = 0
all_movements = []

PIXEL_TO_METER = 0.098e-6
dt = 0.04
T = 293.15     
eta = 0.001     
r = 1.5e-6     
R = 8.314       

while True:

    this_frame_centers = []
    new_active_pollens = {}
    ret, frame = cap.read()

    if current_frame > ending_frame:
        break

    #region frame basic
    frame = frame[60:640,245:852]
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame,(3,3),10)
    #endregion

    #region threshold frame
    _, thresh_frame = cv2.threshold(blur_frame,179,255,cv2.THRESH_BINARY_INV)
    #endregion

    #region contours
    contour_mask_frame = np.zeros(thresh_frame.shape,np.uint8)
    contours, _ = cv2.findContours(thresh_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        if cv2.contourArea(cnt) < 150:
           continue

        cv2.drawContours(contour_mask_frame,[cnt],-1,255,-1)
    #endregion
    
    #region erode
    dist_transform = cv2.distanceTransform(contour_mask_frame,cv2.DIST_L2,5)
    _, sure_fg = cv2.threshold(dist_transform,0.35*dist_transform.max(),255,0)
    #endregion
    
    #region filtering
    sure_fg = np.uint8(sure_fg)
    fg_contours, _ = cv2.findContours(sure_fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #endregion
    
    #region Calculate Brownian Motion
    for fg_cnt in fg_contours:
        
        if cv2.contourArea(fg_cnt) < 5:
            cv2.drawContours(sure_fg, [fg_cnt], -1, 0, -1)
            continue

        moment = cv2.moments(fg_cnt)

        if moment["m00"] != 0:
            cX = int(moment["m10"] / moment["m00"])
            cY = int(moment["m01"] / moment["m00"])

            this_frame_centers.append((cX,cY))

            cv2.circle(contour_mask_frame,(cX,cY),2,125,-1)

    if not active_pollens:
        for center in this_frame_centers:
            new_active_pollens[last_id] = center
            last_id += 1    
    else:

        for center in this_frame_centers:

            closest_id = None
            smallest_distance = 40

            for pollen_id, old_center in active_pollens.items():

                distance = np.sqrt((center[0] - old_center[0])**2 + (center[1] - old_center[1])**2)

                if distance < smallest_distance:
                    smallest_distance = distance
                    closest_id = pollen_id

            if closest_id is not None:
                new_active_pollens[closest_id] = center
                all_movements.append(smallest_distance)
            else:
                new_active_pollens[last_id] = center
                last_id += 1

    active_pollens = new_active_pollens
    #endregion

    #region İd check
    for pollen_id, center in active_pollens.items():
        cv2.putText(contour_mask_frame, f"ID:{pollen_id}", (center[0] - 15, center[1] - 15),
        cv2.FONT_HERSHEY_SIMPLEX, 0.4, 255, 1)
    #endregion
    
    time.sleep(1/25)
    cv2.imshow('test',contour_mask_frame)

    current_frame += 1

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

#region Calculate Avagadro
print("\n" + "="*50)

if len(all_movements) > 0:

    movements_in_meters = np.array(all_movements) * PIXEL_TO_METER

    MSD = np.mean(movements_in_meters ** 2)

    D = MSD / (4 * dt)

    Calculated_avagadro = (R * T) / (6 * np.pi * eta * r * D)

    print(f"Analiz Edilen Toplam Titreşim Verisi: {len(all_movements)} adet")
    print(f"Hesaplanan Difüzyon Katsayısı (D): {D:.4e} m^2/s")
    print(f"Hesaplanan Avagadro Sabiti: {Calculated_avagadro:.4e} mol^-1")
    print(f"Teorik Avogadro Sabiti: 6.022e+23 mol^-1")
    
    deviation = abs(Calculated_avagadro - 6.022e23) / 6.022e23 * 100
    print(f"Teorik Değerden Sapma Oranı: %{deviation:.2f}")
else:
    print("[HATA]")

print("="*50 + "\n")

#endregion



