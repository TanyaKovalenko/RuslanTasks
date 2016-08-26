#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

struct point
{
	float x, y;
};

struct offcut
{
	point A, B;
};

vector<offcut> offcuts;

// The function calculates the vector product
float vectorMulty(float x1, float y1, float x2, float y2)
{

        return x1*y2 - x2*y1;

}

// The function determines whether line segments intersect or not
bool ifCross(float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4)
{
 
        if ( (vectorMulty(x4-x3,y4-y3,x1-x3,y1-y3) * vectorMulty(x4-x3,y4-y3,x2-x3,y2-y3) < 0) &&
             (vectorMulty(x2-x1,y2-y1,x3-x1,y3-y1) * vectorMulty(x2-x1,y2-y1,x4-x1,y4-y1) < 0) )
        {
                return true;
        }

        return false;

}

// The function determines whether 'RED OFFCUT' is visiable from the point O(0,0).

bool isVisible(vector<offcut> &offcuts)
{
        offcut O_Red_A_offcut;
        O_Red_A_offcut.A.x = 0;
        O_Red_A_offcut.A.y = 0;
		O_Red_A_offcut.B.x = offcuts[offcuts.size() - 1].A.x;
        O_Red_A_offcut.B.y = offcuts[offcuts.size() - 1].A.y;

        offcut O_Red_B_offcut;
        O_Red_B_offcut.A.x = 0;
        O_Red_B_offcut.A.y = 0;
		O_Red_B_offcut.B.x = offcuts[offcuts.size() - 1].B.x;
        O_Red_B_offcut.B.y = offcuts[offcuts.size() - 1].B.y;

	float lenAB = sqrt((O_Red_A_offcut.B.x - O_Red_B_offcut.B.x)*(O_Red_A_offcut.B.x - O_Red_B_offcut.B.x) + (O_Red_A_offcut.B.y - O_Red_B_offcut.B.y)*(O_Red_A_offcut.B.y - O_Red_B_offcut.B.y));
	float lenToB = lenAB;
	float lenToA = lenAB;
		
        for (int inx = 0; inx < offcuts.size() - 1; inx++)
        {
			
			// We can assume that the red segment is not visible from the point O 
			// if some of the segments intersects two segments formed by the compound 
			// of the point O to the ends of the red segment. 
			// Those, if the red cuts designated as AB, then if we find a segment that 
			// simultaneously crosses segment OA and OB, the function ifCross should return false. 
				
                if (ifCross(O_Red_A_offcut.A.x, O_Red_A_offcut.A.y, 
							O_Red_A_offcut.B.x, O_Red_A_offcut.B.y, 
							offcuts[inx].A.x, offcuts[inx].A.y, 
							offcuts[inx].B.x, offcuts[inx].B.y) &&
                    ifCross(O_Red_B_offcut.A.x, O_Red_B_offcut.A.y, 
							O_Red_B_offcut.B.x, O_Red_B_offcut.B.y, 
							offcuts[inx].A.x, offcuts[inx].A.y, 
							offcuts[inx].B.x, offcuts[inx].B.y))
				{
                    return false;
				}
				
				// Another case when the red segment is not visible from the point O, 
				// this is the case when there are two pieces, one of them intersects the segment AO, 
				// the second segment overlap BO, and at that, 
				// these two segments intersect inside the triangle AOB.
			
				// x and y are the coordinates of the intersection point for every offcut and segment AB.
				// len is the length from the point (x, y) to the ends of the offcut AB.
				
				float x, y, len;	
 				if (ifCross(O_Red_A_offcut.A.x, O_Red_A_offcut.A.y, 
							O_Red_A_offcut.B.x, O_Red_A_offcut.B.y, 
							offcuts[inx].A.x, offcuts[inx].A.y, 
							offcuts[inx].B.x, offcuts[inx].B.y))
							{
								x = -((O_Red_A_offcut.A.x*O_Red_A_offcut.B.y-O_Red_A_offcut.B.x*O_Red_A_offcut.A.y)*(offcuts[inx].B.x-offcuts[inx].A.x)-
								      (offcuts[inx].A.x*offcuts[inx].B.y-offcuts[inx].B.x*offcuts[inx].A.y)*(O_Red_A_offcut.B.x-O_Red_A_offcut.A.x))/
									  ((O_Red_A_offcut.A.y-O_Red_A_offcut.B.y)*(offcuts[inx].B.x-offcuts[inx].A.x)-(offcuts[inx].A.y-offcuts[inx].B.y)*(O_Red_A_offcut.B.x-O_Red_A_offcut.A.x));
								y = ((offcuts[inx].A.y-offcuts[inx].B.y)*(-x)-(offcuts[inx].A.x*offcuts[inx].B.y-offcuts[inx].B.x*offcuts[inx].A.y))
								     /(offcuts[inx].B.x-offcuts[inx].A.x);
								len = sqrt((x - O_Red_B_offcut.B.x)*(x - O_Red_B_offcut.B.x) + (y - O_Red_B_offcut.B.y)*(y - O_Red_B_offcut.B.y));
								if (len < lenToB)
								{
									lenToB = len;
								}
							}
				if (ifCross(O_Red_B_offcut.A.x, O_Red_B_offcut.A.y, 
							O_Red_B_offcut.B.x, O_Red_B_offcut.B.y, 
							offcuts[inx].A.x, offcuts[inx].A.y, 
							offcuts[inx].B.x, offcuts[inx].B.y))
							{
								x = -((O_Red_B_offcut.A.x*O_Red_B_offcut.B.y-O_Red_B_offcut.B.x*O_Red_B_offcut.A.y)*(offcuts[inx].B.x-offcuts[inx].A.x)-
								      (offcuts[inx].A.x*offcuts[inx].B.y-offcuts[inx].B.x*offcuts[inx].A.y)*(O_Red_B_offcut.B.x-O_Red_B_offcut.A.x))/
									  ((O_Red_B_offcut.A.y-O_Red_B_offcut.B.y)*(offcuts[inx].B.x-offcuts[inx].A.x)-(offcuts[inx].A.y-offcuts[inx].B.y)*(O_Red_B_offcut.B.x-O_Red_B_offcut.A.x));
								y = ((offcuts[inx].A.y-offcuts[inx].B.y)*(-x)-(offcuts[inx].A.x*offcuts[inx].B.y-offcuts[inx].B.x*offcuts[inx].A.y))
								     /(offcuts[inx].B.x-offcuts[inx].A.x);
								len = sqrt((x - O_Red_A_offcut.B.x)*(x - O_Red_A_offcut.B.x) + (y - O_Red_A_offcut.B.y)*(y - O_Red_A_offcut.B.y));
								if (len < lenToA)
								{
									lenToA = len;
								}
							}				
        }
		
		if (lenToA + lenToB < lenAB)
		{
			return false;
		}

        return true;
}

int main() {

        int numOfOffcuts;
        float Ax, Ay, Bx, By;

        cout << "Enter number of offcuts: ";
        cin >> numOfOffcuts;
        cout << "Enter coordinates of the offcuts." << endl;

		// Fill vector of the offcuts.
		// A and B - ends of the every offcuts
		// Ax - x coordonate of the A end (point) of every offcut
		// Bx - x coordonate of the B end (point) of every offcut
        for (int inx = 0; inx < numOfOffcuts; inx++)
        {
				cout << "............Offcut #" << inx << ".........." << endl;
                cout << "Ax = ";
                cin >> Ax;
				cout << "Bx = ";
                cin >> Bx;
                cout << "Ay = ";
                cin >> Ay;
				cout << "By = ";
                cin >> By;
				
				// declare the next offcut
                offcut theOffcut;
                theOffcut.A.x = Ax;
                theOffcut.A.y = Ay;
				theOffcut.B.x = Bx;
                theOffcut.B.y = By;
				
				// push next offcut to the vector
                offcuts.push_back(theOffcut);

        }

        if (isVisible(offcuts))
        {
                cout << "Red offcut is visible from the point O";
        }
        else
        {
                cout << "Red offcut is not visible from the point O";
        }

        return 0;
}

